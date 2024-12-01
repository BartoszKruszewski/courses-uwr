using Microsoft.AspNetCore.Html;
using Microsoft.AspNetCore.Mvc.Rendering;
using System.Linq.Expressions;

namespace WebApplication1.Extensions
{
    public static class HtmlHelperExtensions
    {
        // Wariant 1: Wiązanie nazw pól tekstowych wprost
        public static IHtmlContent Login(this IHtmlHelper htmlHelper, string userNameField, string passwordField)
        {
            var userNameInput = $"<input type=\"text\" name=\"{userNameField}\" />";
            var passwordInput = $"<input type=\"text\" name=\"{passwordField}\" />";
            return new HtmlString($"{userNameInput}{passwordInput}");
        }

        // Wariant 2: Wiązanie przez składowe modelu
        public static IHtmlContent LoginFor<TModel>(this IHtmlHelper<TModel> htmlHelper, Expression<Func<TModel, string>> userNameExpression, Expression<Func<TModel, string>> passwordExpression)
        {
            // Generowanie nazw właściwości modelu
            var userNameField = GetMemberName(userNameExpression);
            var passwordField = GetMemberName(passwordExpression);

            var userNameInput = $"<input type=\"text\" name=\"{userNameField}\" />";
            var passwordInput = $"<input type=\"text\" name=\"{passwordField}\" />";
            return new HtmlString($"{userNameInput}{passwordInput}");
        }

        // Funkcja pomocnicza do pobierania nazwy właściwości z wyrażenia
        private static string GetMemberName<TModel, TProperty>(Expression<Func<TModel, TProperty>> expression)
        {
            var memberExpression = expression.Body as MemberExpression;
            if (memberExpression == null)
                throw new ArgumentException("Expression is not a member expression");
            return memberExpression.Member.Name;
        }
    }
}
