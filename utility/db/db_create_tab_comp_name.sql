CREATE TABLE Company(
    id SERIAL PRIMARY KEY,
    cod_fiscal TEXT NOT NULL,
    nume TEXT,
    stare TEXT,
    tva TEXT,
    loc TEXT,
    sect TEXT,
    str TEXT,
    nr TEXT,
    fax TEXT,
    tel TEXT,
    cp TEXT,
    detalii_adresa TEXT,
    bloc TEXT,
    scara TEXT,
    etaj TEXT,
    ap TEXT
)
