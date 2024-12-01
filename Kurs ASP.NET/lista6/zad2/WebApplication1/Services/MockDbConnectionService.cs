using System.Data.SqlClient;

namespace WebApplication1.Services
{
    public class MockDbConnectionService : IDbConnectionService
    {
        public SqlConnection GetConnection()
        {
            // Symulacja braku połączenia
            throw new NotSupportedException("Symulacja: Brak rzeczywistej bazy danych.");
        }

        public List<Dictionary<string, object>> GetMockData()
        {
            // Symulowane dane
            return new List<Dictionary<string, object>>
        {
            new Dictionary<string, object> { { "Name", "Jan Kowalski" } },
            new Dictionary<string, object> { { "Name", "Anna Nowak" } }
        };
        }
    }
}
