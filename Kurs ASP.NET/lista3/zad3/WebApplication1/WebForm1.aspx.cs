using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string userAgent = Request.Headers["User-Agent"];
            string clientIp = Request.UserHostAddress;

            lblUserAgent.Text = $"User-Agent: {userAgent}";
            lblClientIp.Text = $"Adres IP klienta: {clientIp}";

            string physicalPath = Server.MapPath("~/files");
            lblPhysicalPath.Text = $"Ścieżka fizyczna dla katalogu 'files': {physicalPath}";

            Response.Headers.Add("Custom-Header", "HelloWorld");

            HttpContext currentContext = HttpContext.Current;
            string requestPath = currentContext.Request.Path;
            lblRequestPath.Text = $"Ścieżka żądania: {requestPath}";
        }
    }
}