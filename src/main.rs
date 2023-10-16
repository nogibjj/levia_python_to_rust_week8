// main.rs

use my_project::Database;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let db = Database::new()?;
    let data = db.get_all_data()?;

    for item in data {
        println!("{}", item);
    }

    Ok(())
}
