// main.rs
extern crate rusqlite;
use rusqlite::Result;
use my_db_project::Database;

fn main() -> Result<()> {
    let db = Database::new("my_database.db")?;

    db.insert_user("Alice", "alice@example.com")?;
    db.insert_user("Bob", "bob@example.com")?;

    let users = db.get_users()?;
    for (id, name, email) in users {
        println!("User ID: {}, Name: {}, Email: {}", id, name, email);
    }

    db.update_user(1, "newemail@example.com")?;

    let updated_users = db.get_users()?;
    for (id, name, email) in updated_users {
        println!("Updated User ID: {}, Name: {}, Email: {}", id, name, email);
    }

    Ok(())
}
