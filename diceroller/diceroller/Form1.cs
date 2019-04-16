using System;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace diceroller
{
    public partial class Form1 : Form
    {
        Dicer runner;
        public Form1()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            int dice = Convert.ToInt32(this.textBox1.Text);
            int div = Convert.ToInt32(this.textBox2.Text);
            Dicer runner = new Dicer(0);
            runner.setdiv(div);
            runner.setdice(dice);

            this.textBox3.Text = runner.getWinsS();
            this.textBox4.Text = runner.getAvgS();
            this.textBox5.Text = runner.getBox();
        }
    }

    public class Dicer
    {
        ArrayList box;
        double avg;
        int wins;
        int div;

        public Dicer(int count)
        {
            roller(count);
            this.div = 7;
        }

        private void roller(int count)
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
                else if (temp >= this.div)
                {
                    myList.Add(temp);
                    wins++;
                }
                else if (temp == 1)
                {
                    wins--;
                    myList.Add(temp);
                }
                else if (temp < this.div)
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

        public void setdiv(int div)
        {
            this.div = div;
        }

        public string getBox()
        {
            string output = "";
            sorter();
            foreach (var elements in this.box)
            {
                output = output + elements + ", ";
            }
            return output;
        }

        public int getWins()
        {
            return this.wins;
        }

        public string getWinsS()
        {
            return Convert.ToString(this.wins);
        }

        public double getAvg()
        {
            return this.avg;
        }

        public string getAvgS()
        {
            return Convert.ToString(this.avg);
        }


    }
}
