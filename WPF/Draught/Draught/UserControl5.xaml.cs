using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Draught
{
    /// <summary>
    /// Interaction logic for UserControl5.xaml
    /// </summary>
    public partial class UserControl5 : UserControl
    {
        int[,] cell = new int[10, 10];
        bool[,] king = new bool[10, 10];
        int[] row = new int[50];
        int[] column = new int[50];
        bool mouseMove,enforce,mouseDown;
        int index, count, countGreen, countBlue, reoccur;
        Grid Board = new Grid();
        Label BluePlate, GreenPlate = new Label();
        object[,] tile = new object[10, 10];
        MainWindow remote = new MainWindow();
        enum Mode
        {
            SinglePlayer,
            Multiplayer
        }
        enum Side
        {
            Souce,
            Target
        }
        enum King
        {
            SourceKing,
            TargetKing
        }
        Mode md;
        Side sd;
        
        public UserControl5()
        {
            InitializeComponent();
        }
        public void Logic()
        {
            Random r = new Random();
            int rand = r.Next(0, 51);
            //int m = Random
            for (int i = rand; i < 50; i++)
            {
                
                if (true)
                {
                    if (enforce)
                    {
                        index = reoccur;
                    }
                    if ((king[row[index], column[index]]) && (cell[row[i], column[i]] == 0) && cell[row[index], column[index]] == ((int)sd / 1) + 1)
                    {

                        if (remote.DefineKing(i, index))
                        {
                            ((Label)tile[row[i], column[i]]).Content = ((Label)tile[row[index], column[index]]).Content;
                            ((Label)tile[row[index], column[index]]).Content = "";
                            cell[row[index], column[index]] = 0;
                            cell[row[i], column[i]] = ((int)sd / 1) + 1;
                            king[row[i], column[i]] = true;
                            king[row[index], column[index]] = false;
                            remote.Control();
                            remote.TurnMethod((int)sd);

                        }
                    }
                    ///////////////
                    if (cell[row[index], column[index]] == (((int)sd / 1) + 1) && cell[row[i], column[i]] == 0)
                    {
                        if ((row[i] - row[index] == Math.Pow(-1, (int)sd)) && (Math.Pow(column[i] - column[index], 2) == 1))
                        {
                            //MessageBox.Show("Enforce() is: " + Enforce());
                            if (!remote.Enforce())
                            {
                                ((Label)tile[row[i], column[i]]).Content = ((Label)tile[row[index], column[index]]).Content;
                                cell[row[index], column[index]] = 0;
                                cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                remote.CheckKing((int)sd, i, index);
                                remote.Control();
                                remote.TurnMethod((int)sd);
                            }
                            else
                            {
                                continue;
                            }
                        }
                        else if ((row[index] - row[i] == (4 * (int)sd) - 2) && (Math.Pow(column[i] - column[index], 2) == 4))
                        {
                            // MessageBox.Show("" + column[i] + "\t" + column[index] + "\n" + row[row[index] + 1] + "\t" + column[column[index] + 1] + "\n" + cell[row[index] + 1, column[index] + 1]);
                            if ((column[i] > column[index]) && (cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1] == 2 / ((int)sd + 1)))
                            {
                                bool control = false;
                                ((Label)tile[row[i], column[i]]).Content = ((Label)tile[row[index], column[index]]).Content;
                                ((Label)tile[row[index] - (2 * ((int)sd) - 1), column[index] + 1]).Content = "";
                                cell[row[index], column[index]] = 0;
                                cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1] = 0;
                                remote.deduct((int)sd);
                                ///
                                try
                                {
                                    if (cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && cell[row[i] - (4 * (int)sd - 2), column[i] + 2] == 0)
                                    {
                                        enforce = true;
                                        reoccur = i;
                                        control = true;
                                        break;
                                    }
                                    else
                                        enforce = false;
                                }
                                catch
                                {
                                }
                                try
                                {
                                    if (cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && cell[row[i] - (4 * (int)sd - 2), column[i] - 2] == 0)
                                    {
                                        enforce = true;
                                        reoccur = i;
                                        break;
                                    }
                                    else
                                        enforce = false;
                                }
                                catch
                                {
                                    if (!control)
                                    {
                                        //MessageBox.Show("Maya don happen!!! 1");
                                        enforce = false;
                                        ///
                                        remote.CheckKing((int)sd, i, index);
                                        remote.Control();
                                        remote.TurnMethod((int)sd);
                                        continue;
                                    }
                                }
                                remote.CheckKing((int)sd, i, index);//put a check b$ control meth for continiuty
                                remote.Control();
                                remote.TurnMethod((int)sd);

                            }
                            //MessageBox.Show("row["+index+"] + (int)Math.Pow(-1, "+(int)sd+")" + row[index] +" and "+ (int)Math.Pow(-1, (int)sd));
                            //MessageBox.Show("(column[i] < column[index]) && (cell[row[index] + (int)Math.Pow(-1,(int)sd), column[index] - 1] == 2/((int)sd+1))"+
                            //    (column[i] + "  " + column[index]) + "  " + (cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] + "  " + 2 / ((int)sd + 1))
                            //    );

                            if ((column[i] < column[index]) && (cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] == 2 / ((int)sd + 1)))
                            {
                                bool control = false;
                                ((Label)tile[row[i], column[i]]).Content = ((Label)tile[row[index], column[index]]).Content;
                                ((Label)tile[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1]).Content = "";
                                cell[row[index], column[index]] = 0;
                                cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] = 0;
                                remote.deduct((int)sd);
                                try
                                {
                                    if (cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && cell[row[i] - (4 * (int)sd - 2), column[i] + 2] == 0)
                                    {
                                        enforce = true;
                                        reoccur = i;
                                        control = true;
                                        break;
                                    }
                                    else
                                        enforce = false;
                                }
                                catch { }
                                try
                                {
                                    if (cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && cell[row[i] - (4 * (int)sd - 2), column[i] - 2] == 0)
                                    {
                                        enforce = true;
                                        reoccur = i;
                                        break;
                                    }
                                    else
                                        enforce = false;
                                }
                                catch
                                {
                                    if (!control)
                                    {
                                        //MessageBox.Show("Maya don happen!!! 2");
                                        enforce = false;
                                        remote.CheckKing((int)sd, i, index);
                                        remote.Control();
                                        remote.TurnMethod((int)sd);
                                        continue;
                                    }
                                }
                                remote.CheckKing((int)sd, i, index);
                                remote.Control();
                                remote.TurnMethod((int)sd);
                            }
                        }
                    }


                }
            }
            mouseDown = false;
            mouseMove = false;
            //MessageBox.Show("THIS IS THE PRESENT TURN " + sd);

        }
    }
}
