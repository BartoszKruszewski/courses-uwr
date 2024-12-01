using System.Data.SqlClient;

namespace WebApplication1.Services
{
    
    public interface IDbConnectionService
    {
        SqlConnection GetConnection();
    }

}
