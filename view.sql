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