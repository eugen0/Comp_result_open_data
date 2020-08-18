CREATE TABLE Companie (
	id SERIAL PRIMARY KEY,
	CodFiscal varchar (100) NOT NULL UNIQUE,
	NUME TEXT NOT NULL,
	Stare BOOLEAN,
	TVA BOOLEAN
);

CREATE TABLE CodCaen (
	codCaen_id SERIAL NOT NULL PRIMARY KEY,
	Caen varchar(100),
	Caeno varchar(100),
	companie_id BIGINT REFERENCES Companie(id)
);

CREATE TABLE Contact (
	contact_id serial NOT NULL PRIMARY KEY references Company(id),
	Localitate TEXT ,
	Sector varchar(50) ,
	Str TEXT,
	Nr varchar(50) ,
	Fax varchar(50) ,
	Tel varchar(50) ,
	CodPostal varchar(50) ,
	DetaliiAdresa TEXT ,
	Bloc varchar(50) ,
	Scara varchar(50) ,
	Etaj varchar(50) ,
	Ap varchar(50)
);

CREATE TABLE An (
	id serial NOT NULL PRIMARY KEY,
	An bigint NOT NULL,
	company_id serial NOT NULL references Company(id)
);

CREATE TABLE Profit (
	id serial NOT NULL PRIMARY KEY,
	ProfitBrut bigint,
	ProfitNet bigint
);

CREATE TABLE Pierdere (
	id serial NOT NULL PRIMARY KEY,
	PierdereBrut bigint,
	PierdereNet bigint
);

CREATE TABLE Venit (
	id serial NOT NULL PRIMARY KEY,
	VenitTotal bigint ,
	VenitSpecial bigint ,
	VenitAsigViata bigint,
	VenitAsigGen bigint,
	VenitBrok bigint
);


CREATE TABLE Resultate(
	result_fin_id serial NOT NULL PRIMARY KEY references An(id),
	ActiveImobilizate bigint ,
	ActiveCirculante bigint,
	CheltuieliAvans bigint,
	Datorii bigint,
	VenituriAvans bigint,
	Provisioane bigint,
	Capital bigint,
	Cheltuieli bigint,
	NumarSalariati int,
	venit_id bigint  references Venit(id),
	pierdere_id bigint  references Pierdere(id),
	profit_id bigint  references Profit(id)
);



