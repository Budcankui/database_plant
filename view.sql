CREATE VIEW species_view AS
            SELECT
                cs.species_id,
                cs.species_name,
                cs.species_alias,
                cg.genus_name,
                cf.family_name,
                cs.growth_env,
                cs.province,
                cs.city,
                cs.country
            FROM
                classify_species cs
            JOIN
                classify_genus cg ON cs.genus_id = cg.genus_id
            JOIN
                classify_family cf ON cg.family_id = cf.family_id

-- 植物详细信息视图
CREATE VIEW PlantInfoView AS
SELECT
    ip.plant_id,
    cf.family_name,
    cg.genus_name,
    cs.species_name,
    ip.disease_id,
    pcd.disease_name AS disease_name,
    pcd.method AS disease_control_method,
    ip.plant_desc,
    ip.plant_value,
    ip.plant_tip,
    ip.image_path,
    ip.image_desc,
    ip.image_location
FROM
    info_plant ip
JOIN
    classify_species cs ON ip.species_id = cs.species_id
JOIN
    classify_genus cg ON cs.genus_id = cg.genus_id
JOIN
    classify_family cf ON cg.family_id = cf.family_id
LEFT JOIN
    pest_control_disease pcd ON ip.disease_id = pcd.disease_id;


# 统计每科植物数量
SELECT
    cf.family_name,
    COUNT(cs.species_id) AS plant_count
FROM
    classify_family cf
JOIN
    classify_genus cg ON cf.family_id = cg.family_id
JOIN
    classify_species cs ON cg.genus_id = cs.genus_id
GROUP BY
    cf.family_name;
