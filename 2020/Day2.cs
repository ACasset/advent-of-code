using System.Resources;

class Day2
{
    internal static List<String> ReadInput()
    {
        List<String> input = new List<String>();

        foreach (String line in AdventOfCode.Properties.Resources.Day2.Split("\r\n"))
        {
            input.Add(line);
        }

        return input;
    }

    public static String Step1()
    {
        List<String> input = ReadInput();

        return "";
    }

    public static String Step2()
    {
        List<String> input = ReadInput();

        return "";
    }
}
