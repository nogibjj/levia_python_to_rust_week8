// lib.rs

use rusqlite::{Connection, Result};
use thiserror::Error;

#[derive(Error, Debug)]
enum MyError {
    #[error(transparent)]
    Sqlite(#[from] rusqlite::Error),
}

pub struct Database {
    connection: Connection,
}

impl Database {
    pub fn new() -> Result<Self> {
        let connection = Connection::open("my_database.db")?;
        Ok(Database { connection })
    }

    pub fn get_all_data(&self) -> Result<Vec<String>> {
        let mut stmt = self.connection.prepare("SELECT * FROM my_table")?;
        let data_iter = stmt.query_map([], |row| row.get(0))?;

        let mut result = Vec::new();
        for data in data_iter {
            result.push(data?);
        }

        Ok(result)
    }
}
