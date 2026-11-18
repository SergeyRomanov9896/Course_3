CREATE TABLE companies (
	company_id TEXT NOT NULL PRIMARY KEY,
	company_name TEXT NOT NULL,
	alternate_url TEXT
);

CREATE TABLE vacancies (
	vacancy_id TEXT PRIMARY KEY,
	company_id TEXT NOT NULL,
	vacancy_name TEXT NOT NULL,
	alternate_url TEXT,
	salary_from INT,
	salary_to INT,
	salary_currency CHAR(3),
	salary_gross BOOLEAN,
	FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
