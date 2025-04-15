CREATE TABLE statistics (
    id SERIAL PRIMARY KEY,
    npf_name TEXT,
    assets NUMERIC,
    reserves NUMERIC,
    accumulations NUMERIC,
    npo_clients INTEGER,
    ops_clients INTEGER,
    res_ret_2023 NUMERIC,
    acc_ret_2023 NUMERIC,
    res_ret_2022 NUMERIC,
    acc_ret_2022 NUMERIC
);