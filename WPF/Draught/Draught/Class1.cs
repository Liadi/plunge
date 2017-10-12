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
    class Class1 :MainWindow
    {
        //public override bool enforce;
        
        
        public void Logical(Side state,Window mw)
        {
            
            sd = state;
            Random r = new Random();
            int rand = r.Next(0, 51);
        label: for (int j = rand; j < rand + 50; j++)
            {
                int i = 0 ;
                int index = j % 50;
                for (int k = 0; k < 4; ++k)
                {
                    if (row[index] % 2 != 0)
                    {
                        switch (k)
                        {
                            case 0:
                                i = index - 4;//
                                break;
                            case 1:
                                i = index - 5;//
                                break;
                            case 2:
                                i = index - 9;//
                                break;
                            case 3:
                                i = index - 11;//
                                break;
                        }
                    }
                    if (row[index] % 2 == 0)
                    {
                        switch (k)
                        {
                            case 0:
                                i = index - 5;//
                                break;
                            case 1:
                                i = index - 6;//
                                break;
                            case 2:
                                i = index - 9;//
                                break;
                            case 3:
                                i = index - 11;//
                                break;
                        }
                    }

                    if ((i >= 0) && (i < 50))//Board.Children[i].IsMouseOver && mouseMove
                    {
                        //MessageBox.Show("the state of index (" + index + ") and i (" + i + ") resp is:  "
                        //    + ((MainWindow)mw).cell[row[index], column[index]] + "&" + ((MainWindow)mw).cell[row[i], column[i]]);
                        if (enforce)
                        {
                            index = reoccur;
                        }
                        //try
                        if ((((MainWindow)mw).king[row[index], column[index]]) && (((MainWindow)mw).cell[row[i], column[i]] == 0) && ((MainWindow)mw).cell[row[index], column[index]] == ((int)sd / 1) + 1)
                        {

                            if (((MainWindow)mw).DefineKing(i, index))
                            {
                                ((MainWindow)mw).setcolor(index);
                                ((Label)((MainWindow)mw).tile[row[i], column[i]]).Content = ((Label)((MainWindow)mw).tile[row[index], column[index]]).Content;
                                ((Label)((MainWindow)mw).tile[row[index], column[index]]).Content = "";
                                ((MainWindow)mw).cell[row[index], column[index]] = 0;
                                ((MainWindow)mw).cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                ((MainWindow)mw).king[row[i], column[i]] = true;
                                ((MainWindow)mw).king[row[index], column[index]] = false;
                                //Control();
                                //TurnMethod((int)sd);
                                
                            }
                        }
                        //MessageBox.Show("state is: "+sd);
                        if (((MainWindow)mw).cell[row[index], column[index]] == (((int)sd / 1) + 1) && ((MainWindow)mw).cell[row[i], column[i]] == 0)
                        {
                            if ((row[i] - row[index] == Math.Pow(-1, (int)sd)) && (Math.Pow(column[i] - column[index], 2) == 1))
                            {
                                //MessageBox.Show("Enforce() is: " + ((MainWindow)mw).Enforce());
                                if (!((MainWindow)mw).Enforce())
                                {
                                    ((MainWindow)mw).setcolor(index);
                                    ((Label)((MainWindow)mw).tile[row[i], column[i]]).Content = ((Label)((MainWindow)mw).tile[row[index], column[index]]).Content;
                                    ((MainWindow)mw).cell[row[index], column[index]] = 0;
                                    ((MainWindow)mw).cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                    ((MainWindow)mw).CheckKing((int)sd, i, index);
                                    //((MainWindow)mw).Control();
                                    //TurnMethod((int)sd);
                                    goto exit;
                                }
                                else
                                {
                                    if (k<4)
                                        continue;
                                    rand = ++index;
                                    goto label; //continue
                                }
                            }
                           
                            else if ((row[index] - row[i] == (4 * (int)sd) - 2) && (Math.Pow(column[i] - column[index], 2) == 4))
                            {
                                //MessageBox.Show("'index' and 'i' is: "+index+" and "+i+" resp.");
                                //try
                                //{
                                if 
                                    
                                    ((column[i] > column[index]) && ((((MainWindow)mw).cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1] == 2 / ((int)sd + 1))||
                                    (((MainWindow)mw).cell[row[index] + (2 * ((int)sd) - 1), column[index] + 1] == 2 / ((int)sd + 1))
                                    ))
                                {
                                    bool control = false;
                                    ((MainWindow)mw).setcolor(index);
                                    int holder = 0;
                                    object place = null;
                                    if (((int)sd == 1 && row[i] < row[index]) || ((int)sd == 0 && row[i] > row[index]))
                                        //(((MainWindow)mw).cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1] == 2 / ((int)sd + 1))

                                    {
                                        ((MainWindow)mw).cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1] = holder;
                                        ((Label)((MainWindow)mw).tile[row[index] - (2 * ((int)sd) - 1), column[index] + 1]).Content = place;
                                    }
                                    else
                                    {
                                        ((MainWindow)mw).cell[row[index] + (2 * ((int)sd) - 1), column[index] + 1] = holder;
                                        ((Label)((MainWindow)mw).tile[row[index] + (2 * ((int)sd) - 1), column[index] + 1]).Content = place;
                                    }
                                    //MessageBox.Show("Just before the break point!!!");
                                    ((Label)((MainWindow)mw).tile[row[i], column[i]]).Content = ((Label)((MainWindow)mw).tile[row[index], column[index]]).Content;
                                    //((Label)((MainWindow)mw).tile[row[index] - (2 * ((int)sd) - 1), column[index] + 1]).Content = "";
                                    place = "";
                                    ((MainWindow)mw).cell[row[index], column[index]] = 0;
                                    ((MainWindow)mw).cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                    //((MainWindow)mw).cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1] = 0;
                                    holder = 0;
                                    ((MainWindow)mw).deduct((int)sd);
                                    ///
                                    try
                                    {
                                        if ((((MainWindow)mw).cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] - (4 * (int)sd - 2), column[i] + 2] == 0)||
                                            (((MainWindow)mw).cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] + (4 * (int)sd - 2), column[i] + 2] == 0)
                                            )
                                        {
                                            enforce = true;
                                            reoccur = i;
                                            control = true;
                                            continue; //break
                                        }
                                        else
                                            enforce = false;
                                    }
                                    catch
                                    {
                                    }
                                    try
                                    {
                                        if ((((MainWindow)mw).cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] - (4 * (int)sd - 2), column[i] - 2] == 0)||
                                            (((MainWindow)mw).cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] + (4 * (int)sd - 2), column[i] - 2] == 0)
                                            )
                                        {
                                            enforce = true;
                                            reoccur = i;
                                            continue;//break
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
                                            ((MainWindow)mw).CheckKing((int)sd, i, index);
                                            //Control();
                                            //TurnMethod((int)sd);
                                            //goto label; //continue;
                                        }
                                    }
                                    ((MainWindow)mw).CheckKing((int)sd, i, index);//put a check b$ control meth for continiuty
                                    goto exit;
                                    //Control();
                                    //TurnMethod((int)sd);

                                }

                                if ((column[i] < column[index]) && 
                                    ((((MainWindow)mw).cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] == 2 / ((int)sd + 1))||
                                    (((MainWindow)mw).cell[row[index] - (int)Math.Pow(-1, (int)sd), column[index] - 1] == 2 / ((int)sd + 1))
                                    )
                                    )
                                {
                                    bool control = false;
                                    ((MainWindow)mw).setcolor(index);
                                    int holder = 0;
                                    object place = null;
                                    if (((int)sd == 1 && row[i] < row[index]) || ((int)sd == 0 && row[i] > row[index]))
                                        //((((MainWindow)mw).cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] == 2 / ((int)sd + 1)))
                                    {
                                        ((MainWindow)mw).cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] = holder;
                                        ((Label)((MainWindow)mw).tile[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1]).Content = place;
                                    }
                                    else
                                    {
                                        ((MainWindow)mw).cell[row[index] - (int)Math.Pow(-1, (int)sd), column[index] - 1] = holder;
                                        ((Label)((MainWindow)mw).tile[row[index] - (int)Math.Pow(-1, (int)sd), column[index] - 1]).Content = place;
                                    }
                                    //MessageBox.Show("Just b4 break point");
                                    ((Label)((MainWindow)mw).tile[row[i], column[i]]).Content = ((Label)((MainWindow)mw).tile[row[index], column[index]]).Content;
                                    //((Label)((MainWindow)mw).tile[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1]).Content = "";
                                    place = "";
                                    ((MainWindow)mw).cell[row[index], column[index]] = 0;
                                    ((MainWindow)mw).cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                    //((MainWindow)mw).cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] = 0;
                                    holder = 0;
                                    ((MainWindow)mw).deduct((int)sd);
                                    try
                                    {
                                        if ((((MainWindow)mw).cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] - (4 * (int)sd - 2), column[i] + 2] == 0)||
                                            (((MainWindow)mw).cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] + (4 * (int)sd - 2), column[i] + 2] == 0)
                                            )
                                        {
                                            enforce = true;
                                            reoccur = i;
                                            control = true;
                                            continue;// goto exit;// break;
                                        }
                                        else
                                            enforce = false;
                                    }
                                    catch { }
                                    try
                                    {
                                        if ((((MainWindow)mw).cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] - (4 * (int)sd - 2), column[i] - 2] == 0)||
                                            (((MainWindow)mw).cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && ((MainWindow)mw).cell[row[i] + (4 * (int)sd - 2), column[i] - 2] == 0))
                                        {
                                            enforce = true;
                                            reoccur = i;
                                            continue;//goto exit;// break;
                                        }
                                        else
                                            enforce = false;
                                    }
                                    catch
                                    {
                                        if (!control)// the if condition makes the catch for the two try
                                        {
                                            //MessageBox.Show("Maya don happen!!! 2");
                                            enforce = false;
                                            ((MainWindow)mw).CheckKing((int)sd, i, index);
                                            //Control();
                                            //TurnMethod((int)sd);
                                            //goto exit; // continue;///////////////////////////
                                        }
                                    }
                                    ((MainWindow)mw).CheckKing((int)sd, i, index);
                                    goto exit;
                                    //Control();
                                    //TurnMethod((int)sd);
                                }
                            //}
                                //catch
                                //{
                                //    MessageBox.Show("maya don happen 4 comp!!!");
                                //    goto label;
                                    
                                //}
                            }
                            
                        }


                    }
                    else  
                        continue; 
                }//end inner loop
            }//end outer loop
            exit:mouseDown = false;
            mouseMove = false;

        }
  
    }

}
