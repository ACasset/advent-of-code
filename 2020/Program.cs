using System.Reflection;

Console.WriteLine("Choose day [1-25]");
String? dayInput = Console.ReadLine();
Console.WriteLine();

Int32 day;

if (!Int32.TryParse(dayInput, out day) || day < 1 || day > 25)
{
    return -1;
}

Console.WriteLine("Choose step [1-2]");
String? stepInput = Console.ReadLine();
Console.WriteLine();

Int32 step;

if (!Int32.TryParse(stepInput, out step) || step < 1 || step > 25)
{
    return -2;
}

Type? type = Type.GetType("Day" + day);

if (type == null)
{
    return -3;
}

MethodInfo? methodInfo = type.GetMethod("Step" + step);

if (methodInfo == null)
{
    return -4;
}

object? result = methodInfo.Invoke(null, null);

if (result == null)
{
    return -5;
}

Console.WriteLine("Day {0}, step {1} = " + result.ToString(), day, step);

return 0;