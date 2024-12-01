using System.Data.SqlClient;
using Microsoft.Extensions.Configuration;

namespace WebApplication1.Services
{
    public class DbConnectionService : IDbConnectionService
    {
        private readonly string _connectionString;

        public DbConnectionService(IConfiguration configuration)
        {
            // Pobranie connection stringa z konfiguracji
            _connectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public SqlConnection GetConnection()
        {
            return new SqlConnection(_connectionString);
        }
    }
}
