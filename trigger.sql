CREATE TRIGGER tr_RecordMonitorException
ON monitor_data
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Record exceptions for temperature
    INSERT INTO monitor_exception (data_id, exception_index, exception_value)
    SELECT i.data_id, 'temperature_high', i.index_temperature
    FROM inserted i
    LEFT JOIN deleted d ON i.data_id = d.data_id
    WHERE i.index_temperature > 35 AND (d.index_temperature IS NULL OR d.index_temperature <= 35);

    INSERT INTO monitor_exception (data_id, exception_index, exception_value)
    SELECT i.data_id, 'temperature_low', i.index_temperature
    FROM inserted i
    LEFT JOIN deleted d ON i.data_id = d.data_id
    WHERE i.index_temperature < -15 AND (d.index_temperature IS NULL OR d.index_temperature >= -15);

    -- Record exceptions for humidity
    INSERT INTO monitor_exception (data_id, exception_index, exception_value)
    SELECT i.data_id, 'humidity_high', i.index_humidity
    FROM inserted i
    LEFT JOIN deleted d ON i.data_id = d.data_id
    WHERE i.index_humidity > 90 AND (d.index_humidity IS NULL OR d.index_humidity <= 90);

    INSERT INTO monitor_exception (data_id, exception_index, exception_value)
    SELECT i.data_id, 'humidity_low', i.index_humidity
    FROM inserted i
    LEFT JOIN deleted d ON i.data_id = d.data_id
    WHERE i.index_humidity < 20 AND (d.index_humidity IS NULL OR d.index_humidity >= 20);
END;
