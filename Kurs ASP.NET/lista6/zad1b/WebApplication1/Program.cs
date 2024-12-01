using WebApplication1;
using WebApplication1.Controllers;
var builder = WebApplication.CreateBuilder(args);
var services = builder.Services;
services.AddControllersWithViews();
services.AddSingleton<CMSCustomRouteTransformer>();
var app = builder.Build();
app.UseRouting();
app.UseEndpoints(endpoints =>
    {
        endpoints.MapDynamicControllerRoute<CMSCustomRouteTransformer>("CMS/{**sitepage}" );
        endpoints.MapControllerRoute(
        name: "default",
        pattern: "{controller=Page}/{action=Render}/{id?}");
    }
);
app.Run();