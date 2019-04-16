using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpyTester
{
    class Program
    {        
        static void Main(string[] args)
        {
            int count = 0;
            Dicer runner = new Dicer(count);

            while (count != -1)
            {
                if(count == -1)
                { break; }

                Console.WriteLine("Enter Amount of dice to roll");
                string userinput = Console.ReadLine();
                count = Convert.ToInt32(userinput);

                runner.setdice(count);

                runner.printer();
                Console.ReadKey();

            }
        }
    }


    public class Dicer
    {
        ArrayList box;
        double avg;
        int wins;

        public Dicer(int count)
        {
            roller(count);
        }

        private void roller( int count)
        {
            Random rnd = new Random();
            ArrayList myList = new ArrayList();
            int wins = 0;
            int temp = 0;
            for (int a = 0; a < count; a++)
            {
                temp = rnd.Next(1, 10);

                if (temp == 10)
                {
                    a = a - 1;
                    wins++;
                    myList.Add(temp);
                }
                else if (temp >= 7)
                {
                    myList.Add(temp);
                    wins++;
                }
                else if (temp == 1)
                {
                    wins--;
                    myList.Add(temp);
                }
                else if (temp < 7)
                {
                    myList.Add(temp);
                }
                //myList.Add(rnd.Next(1,10));
            }
            this.box = myList;
            this.wins = wins;
            avager();

        }

        private void avager()
        {
            double avg = 0.0;
            foreach (int elements in this.box)
            {
                avg = avg + elements;
            }
            avg = avg / this.box.Count;
            this.avg = avg;
        }

        private void sorter()
        {
                for (int i = 0; i < this.box.Count - 1; i++)
                {
                    for (int j = this.box.Count - 1; j > i; j--)
                    {
                        if (Convert.ToInt32(this.box[j]) < Convert.ToInt32(this.box[j - 1]))
                        {
                            int x = Convert.ToInt32(this.box[j]);
                            this.box[j] = this.box[j - 1];
                            this.box[j - 1] = x;

                        }
                    }
                }
        }

        public void printer()
        {
            sorter();
            Console.WriteLine("The dice rolled");
            foreach (var elements in this.box)
            {
                Console.Write(elements + ", ");
            }
            Console.WriteLine();
            Console.WriteLine("Wins: " + this.wins);
            Console.WriteLine("Avg: " + this.avg);
        }

        public void setdice(int count)
        {
            roller(count);
        }

    }
}
