using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication1
{
    public class CustomHttpHandler : IHttpHandler
    {
        #region IHttpHandler Members
        public bool IsReusable
        {
            get { return true; }
        }
        public void ProcessRequest(HttpContext context)
        {
            var routeData = context.Request.RequestContext.RouteData.Values;
            string response =
            (string.Format("tenant: {0} site: {1} page: {2}", routeData["tenant"], routeData["siteName"], routeData["pageName"] ) );
            context.Response.Write(response);
        }
        #endregion
    }
}