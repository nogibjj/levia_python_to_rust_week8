// main.rs
use my_project::database::DbConnection;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let database_url = "your_database_url_here";
    let connection = DbConnection::new(database_url).await?;

    let data = connection.get_data().await?;
    
    // Process the data as needed

    Ok(())
}
