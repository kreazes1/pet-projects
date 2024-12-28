using System;

namespace project {

    class Program {

        static void Main() {
            int[] array = [1, 2, 3, 4];
            
            Console.Write("Press any key...");
            Console.ReadKey();
            Console.Clear();

            Console.Write("1. Плюс \n2. Минус \n3. Умножение \n4. Деление \nВыберите пункт: ");
            byte user_select = Convert.ToByte(Console.ReadLine());

            switch (user_select)
            {
                case 1: Plus();
                break;
                case 2: Minus();
                break;
                case 3: Umn();
                break;
                case 4: Del();
                break;
            } if (!Array.Exists(array, element => element == user_select)) {
                Console.WriteLine("Введено неверное значение!");
            }

        }

        public static void Plus() {
            Console.Write("Введите число: ");
            float user_input_plus = float.Parse(Console.ReadLine());
            Console.Write("Введите второе число: ");
            float user_input_plus2 = float.Parse(Console.ReadLine());
            Console.WriteLine("Результат прибавления двух чисел: {0}", user_input_plus + user_input_plus2);
        }

        public static void Minus() {
            Console.Write("Введите число: ");
            float user_input_minus = float.Parse(Console.ReadLine());
            Console.Write("Введите второе число: ");
            float user_input_minus2 = float.Parse(Console.ReadLine());
            Console.WriteLine("Результат минусования двух чисел: {0}", user_input_minus - user_input_minus2);
        }

        public static void Umn() {
            Console.Write("Введите число: ");
            float user_input_umn = float.Parse(Console.ReadLine());
            Console.Write("Введите второе число: ");
            float user_input_umn2 = float.Parse(Console.ReadLine());
            Console.WriteLine("Результат умножения двух чисел: {0}", user_input_umn * user_input_umn2);
        }

        public static void Del() {
            Console.Write("Введите число: ");
            float user_input_del = float.Parse(Console.ReadLine());
            Console.Write("Введите второе число: ");
            float user_input_del2 = float.Parse(Console.ReadLine());
            Console.WriteLine("Результат деления двух чисел: {0}", user_input_del / user_input_del2);
        }
    }
}