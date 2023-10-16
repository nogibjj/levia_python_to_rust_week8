use rusqlite::{Connection, Result};

pub struct Database {
    conn: Connection,
}

impl Database {
    pub fn new(db_file: &str) -> Result<Database> {
        let conn = Connection::open(db_file)?;
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )",
            [] 
        )?;
        Ok(Database { conn })
    }

    

    pub fn insert_user(&self, name: &str, email: &str) -> Result<()> {
        self.conn.execute(
            "INSERT INTO users (name, email) VALUES (?1, ?2)",
            &[name, email]
        )?;
        Ok(())
    }


    pub fn get_users(&self) -> Result<Vec<(i64, String, String)>> {
        let mut stmt = self.conn.prepare("SELECT id, name, email FROM users")?;
        let user_iter = stmt.query_map([], |row| Ok((row.get(0)?, row.get(1)?, row.get(2)?)))?;

        let mut users = Vec::new();
        for user in user_iter {
            users.push(user?);
        }
        Ok(users)
    }


    pub fn update_user(&self, id: i64, new_email: &str) -> Result<()> {
    self.conn.execute(
        "UPDATE users SET email = ?1 WHERE id = ?2",
        &[new_email as &dyn rusqlite::ToSql, &id as &dyn rusqlite::ToSql]
    )?;
    Ok(())
}



}
