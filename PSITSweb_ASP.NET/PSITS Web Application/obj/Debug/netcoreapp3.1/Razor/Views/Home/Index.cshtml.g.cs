#pragma checksum "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\Home\Index.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "52192b656766cb8b608d4092862f88fc63722241"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Home_Index), @"mvc.1.0.view", @"/Views/Home/Index.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\_ViewImports.cshtml"
using PSITS_Web_Application;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\_ViewImports.cshtml"
using PSITS_Web_Application.Models;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\_ViewImports.cshtml"
using PSITS_Web_Application.ViewModels;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\_ViewImports.cshtml"
using PSITS_Web_Application.Models.Auth;

#line default
#line hidden
#nullable disable
#nullable restore
#line 6 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\_ViewImports.cshtml"
using PSITSWeb_ASP.NET.data.Models.Entity;

#line default
#line hidden
#nullable disable
#nullable restore
#line 7 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\_ViewImports.cshtml"
using PSITSWeb_ASP.NET.data.Models.Objects;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"52192b656766cb8b608d4092862f88fc63722241", @"/Views/Home/Index.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"feed140d9ed03e677832a6128d52db7f00256909", @"/Views/_ViewImports.cshtml")]
    public class Views_Home_Index : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<HomeViewModel>
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#nullable restore
#line 2 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\Home\Index.cshtml"
  
    ViewData["Title"] = "PSITS";

#line default
#line hidden
#nullable disable
            WriteLiteral("<br /><br /><br /><br /><br /><br />\r\n<div class=\"text-center\">\r\n");
#nullable restore
#line 7 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\Home\Index.cshtml"
      
        foreach(var announcement in await Model.GetAnnouncementsAsync())
            {

#line default
#line hidden
#nullable disable
            WriteLiteral("                <h1 class=\"display-4\">");
#nullable restore
#line 10 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\Home\Index.cshtml"
                                 Write(announcement.Title);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h1>\r\n                <h5>");
#nullable restore
#line 11 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\Home\Index.cshtml"
               Write(announcement.Content);

#line default
#line hidden
#nullable disable
            WriteLiteral("</h5>\r\n");
#nullable restore
#line 12 "D:\Important\Programming Langs\Python\PSITS\PSITSWebApp\PSITSweb_ASP.NET\PSITS Web Application\Views\Home\Index.cshtml"
            }
    

#line default
#line hidden
#nullable disable
            WriteLiteral("    <p>Retrieved from PSITS Database</p>\r\n    <p>Learn about <a href=\"https://docs.microsoft.com/aspnet/core\">building Web apps with ASP.NET Core</a>.</p>\r\n</div>\r\n<br /><br /><br /><br /><br /><br />\r\n");
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<HomeViewModel> Html { get; private set; }
    }
}
#pragma warning restore 1591
