using System.Resources;

class Day1
{
    internal static List<Int32> ReadInput()
    {
        List<Int32> input = new List<Int32>();

        foreach (String line in AdventOfCode.Properties.Resources.Day1.Split("\r\n"))
        {
            input.Add(Int32.Parse(line));
        }

        return input;
    }

    public static String Step1()
    {
        List<Int32> input = ReadInput();

        for (Int32 i = 0; i < input.Count; i++)
        {
            for (Int32 j = i + 1; j < input.Count; j++)
            {
                if (input[i] + input[j] == 2020)
                {
                    return (input[i] * input[j]).ToString();
                }
            }
        }

        return "";
    }

    public static String Step2()
    {
        List<Int32> input = ReadInput();

        for (Int32 i = 0; i < input.Count; i++)
        {
            for (Int32 j = i + 1; j < input.Count; j++)
            {
                for (Int32 k = j + 1; k < input.Count; k++)
                {
                    if (input[i] + input[j] + input[k] == 2020)
                    {
                        return (input[i] * input[j] * input[k]).ToString();
                    }
                }
            }
        }

        return "";
    }
}
