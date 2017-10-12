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
using System.Timers;

namespace Draught
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public int[] state = new int [50];//if 0 "zero", tile is empty; if 1 "one", tile has sideA's piece; if 2 "two", tile has sideB's piece
        public bool mouseMove, mouseDown, set, start, enforce;
        public object[,] tile = new object[10, 10];
        public int[,] cell = new int[10, 10];
        public bool[,] king = new bool[10, 10];
        public int[] row = new int[50];
        public int[] column = new int[50];
        public int index, count, countGreen, countBlue, reoccur;
        public Mode md;
        public Side sd ;
        
        public MainWindow()
        {
            InitializeComponent();
            SetRowColumn();
            BluePlate.Content = countBlue;
            GreenPlate.Content = countGreen;
        }
        
        public enum Mode 
        {
            SinglePlayer,
            Multiplayer
        }
        
        public enum Side 
        {
            Source,
            Target
        }
        
        enum King 
        {
            SourceKing,
            TargetKing
        }

        public void Board_MouseDown_1(object sender, MouseButtonEventArgs e)
        {
            
            if (set)
            {
                for (int i = 0; i < 50; i++)
                {
                    if (Board.Children[i].IsMouseOver)
                    {
                        mouseDown = true;
                        index = i;
                        break;
                    }
                }
            }
            else
                MessageBox.Show("Pick a Game Type in 'Start Game' to begin");
        }
                 
        public void Board_MouseMove_1(object sender, MouseEventArgs e)
        {
           
            if (mouseDown) 
            {
               
                    if (cell[row[index],column[index]] == (int)sd+1)
                    {
                        //MessageBox.Show(""+(((Label)tile[row[index], column[index]]).Content).GetType());

                        
                        //e.GetPosition(main);
                        //Canvas.SetLeft((Label)tile[row[index], column[index]]).Content, e.GetPosition(Board).X - 25);
                        //Canvas.SetTop((UIElement)(((Label)tile[row[index], column[index]]).Content), e.GetPosition(Board).Y - 25);
                       
                        //e.GetPosition(main);
                        //Canvas.SetLeft((Ellipse)((Shape)(((UserControl)(((Label)tile[row[i], column[i]]).Content)).c)), e.GetPosition(Board).X - 25);
                        //Canvas.SetTop((Control)(((Label)tile[row[i], column[i]]).Content), e.GetPosition(Board).Y - 25);
                    }
                
                mouseMove = true;
                    
            }
            
        }

        public void Board_MouseUp_1(object sender, MouseButtonEventArgs e)
        {
            if ((int)md == 0 && (int)sd==0) 
            {
                Side player = sd;
                Logic((int)md);
                if (sd != player)
                {
                    Class1 comp = new Class1();
                    //MessageBox.Show("Computer about to play!!! \n pls wait");
                    //comp.Logically(md, this);
                    comp.Logical(sd, this);
                    Control();
                    TurnMethod((int)sd);
                    ///MessageBox.Show("Computer is done!!! \n pls play");
                }
            }
            else if ((int)md == 1)
            {
                
                Logic((int)md);
            }
        }

        public void Single_Click(object sender, RoutedEventArgs e)
        {
            if (!start)
            {
                md = Mode.SinglePlayer;
                MessageBox.Show("SINGLE Player");
                MessageBox.Show("Still in progress...");
                set = true;
                TurnMethod((int)sd);
            }
            start = true;
        }

        public void Multiple_Click(object sender, RoutedEventArgs e)
        {
            if (!start)
            {
                md = Mode.Multiplayer;
                MessageBox.Show("DOUBLE Players");
                set = true;
                TurnMethod((int)sd);
            }
            start = true;
        }
        //controls the turn of the players
        public void Control() 
        {
            count = count + 1;
            sd = (Side)((count) % 2);
        }
        //method enforcing movement rules
        public Boolean Enforce() 
        {
            bool value = false;
            bool another = false;
                for (int i = 0; i < 50; i++)
                {
                    try
                    {
                        if ((cell[row[i], column[i]] == (int)sd + 1) && 
                            (
                            ((cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1)) && (cell[row[i] - ((4 * (int)sd)-2), column[i] + 2] == 0))||
                            ((cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1)) && (cell[row[i] + ((4 * (int)sd) - 2), column[i] + 2] == 0))
                            ))
                            {
                            
                                value = true;
                                another = true;
                                if ((cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1)) && (cell[row[i] - ((4 * (int)sd) - 2), column[i] + 2] == 0))
                                {
                                    ((Label)tile[row[i] - ((4 * (int)sd) - 2), column[i] + 2]).Background = Brushes.Aqua;
                                }
                                else 
                                {
                                    ((Label)tile[row[i] + ((4 * (int)sd) - 2), column[i] + 2]).Background = Brushes.Aqua;
                                }
                            }
                    }
                    catch
                    {

                    }
                    try{
                        if ((cell[row[i], column[i]] == (int)sd+1) && 
                            (
                            ((cell[row[i] +(int)Math.Pow(-1, (int)sd), column[i] - 1] == 2/((int)sd+1)) && (cell[row[i] - (4*(int)sd-2), column[i] - 2] == 0))||
                            ((cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1)) && (cell[row[i] + (4 * (int)sd - 2), column[i] - 2] == 0))
                            )
                            )//////////////
                            {
                                value = true;
                               // MessageBox.Show("print " + i);
                                if ((cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1)) && (cell[row[i] - (4 * (int)sd - 2), column[i] - 2] == 0))
                                {
                                    ((Label)tile[row[i] - (4 * (int)sd - 2), column[i] - 2]).Background = Brushes.Aqua;
                                }
                                else 
                                {
                                    ((Label)tile[row[i] + (4 * (int)sd - 2), column[i] - 2]).Background = Brushes.Aqua;
                                }
                                continue;
                            }
                        else if (another) 
                        {
                            continue;
                        }
                    }
                    catch 
                    {
                        continue;
                    }
                }
            
            
            //MessageBox.Show("return is:\t"+value);
            return value;
        }

        public void TurnMethod(int n) 
        {
            if (n == 0)
                ((Rectangle)Turn.Children[1]).Fill = Brushes.GreenYellow;
            else if (n == 1)
                ((Rectangle)Turn.Children[1]).Fill = Brushes.Blue;
        }
        public void CheckKing( int enumerator,int target,int source) 
        {
            if (!enforce)
            {

                if (enumerator == 0 && row[target] == 9)
                {
                    ((Label)tile[row[target], column[target]]).Content = new UserControl1();
                    ((Label)tile[row[source], column[source]]).Content = "";
                    cell[row[target], column[target]] = 1;
                    cell[row[source], column[source]] = 0;
                    king[row[target], column[target]] = true;
                }
                else if (enumerator == 1 && row[target] == 0)
                {
                    ((Label)tile[row[target], column[target]]).Content = new UserControl4();
                    ((Label)tile[row[source], column[source]]).Content = "";
                    cell[row[target], column[target]] = 2;
                    cell[row[source], column[source]] = 0;
                    king[row[target], column[target]] = true;
                }
            }
        }

        /// <summary>
        /// Board setup.
        /// Assign to each cell in the grid a column and a row
        /// Create Object of tiles and put in opposite sides (Blue and Green)
        /// 20 tiles on each side
        /// </summary>
        public void SetRowColumn()
        {
            for (int cellIndex = 0; cellIndex < 50; cellIndex++) 
            {
                //Board.Children[cellIndex] = null;
                

                int j = cellIndex % 10;
                switch(j)
                {
                    case 0:
                        column[cellIndex] = 0;
                        break;
                    case 1:
                        column[cellIndex] = 2;
                        break;
                    case 2:
                        column[cellIndex] = 4;
                        break;
                    case 3:
                        column[cellIndex] = 6;
                        break;
                    case 4:
                        column[cellIndex] = 8;
                        break;
                    case 5:
                        column[cellIndex] = 1;
                        break;
                    case 6:
                        column[cellIndex] = 3;
                        break;
                    case 7:
                        column[cellIndex] = 5;
                        break;
                    case 8:
                        column[cellIndex] = 7;
                        break;
                    case 9:
                        column[cellIndex] = 9;
                        break;
                        
                }
       
                if (cellIndex < 20)
                {
                    
                    row[cellIndex] = cellIndex / 5;
                    cell[row[cellIndex], column[cellIndex]] = 1;
                    tile[row[cellIndex], column[cellIndex]] = Board.Children[cellIndex];
                    
                    ((Label)tile[row[cellIndex],column[cellIndex]]).Content = new UserControl2();
                    countGreen++;
                    
                }
                else if (cellIndex >= 20 && cellIndex < 25)
                {
                    row[cellIndex] = 4;
                    tile[row[cellIndex], column[cellIndex]] = Board.Children[cellIndex];
                    ((Label)tile[row[cellIndex], column[cellIndex]]).Content = "";
                    //tile[row[cellIndex], column[cellIndex]] = null;
                    
                    
                }
                else if (cellIndex >= 25 && cellIndex < 30)
                {
                    row[cellIndex] = 5;
                    tile[row[cellIndex], column[cellIndex]] = Board.Children[cellIndex];
                    ((Label)tile[row[cellIndex], column[cellIndex]]).Content = "";
                    //tile[row[cellIndex], column[cellIndex]] = null;
                    
                    
                }
                else if (cellIndex >= 30 && cellIndex < 50)
                {
                   
                    
                    row[cellIndex] = cellIndex / 5;
                    cell[row[cellIndex], column[cellIndex]] = 2;
                     tile[row[cellIndex], column[cellIndex]] = Board.Children[cellIndex];
                   ((Label)tile[row[cellIndex], column[cellIndex]]).Content = new UserControl3();
                    countBlue++;
                    
                }
            }
            setcolor(-1);
        }
        public Boolean DefineKing(int target, int source ) 
        {
            bool ret = true;
            int [] hor = new int [50];
            int[] ver = new int[50];
            hor = row;
            ver = column;
            if (hor[target] > hor[source] && ver[target] > ver[source])//south east
            {
                
                for (int m = 1; m <= (hor[target] - hor[source] - 1); m++) 
                {
                    int localRow = m+hor[source];
                    int localCol = m+ver[source];
                   // MessageBox.Show("localCol localRow hor[source] ver[source] is: " + localCol + "\t " + localRow + "\t " + hor[source] + "\t " + ver[source]);
                    if (cell[localRow, localCol] == (((int)sd + 1) % 2) + 1) //if another tile
                    {
                        if (ret == false) 
                        {
                            break;
                        }
                        for (int n = 1; n <= (row[target] - row[source] - 1-m); n++) 
                        {
                     //       MessageBox.Show("cell["+(n+localRow)+", "+(n+localCol)+"] is: " + cell[(n + localRow), (n + localCol)]);
                            if (cell[(n+localRow), (n+localCol)] == 0)
                                continue;
                            else
                                ret = false;
                            break;

                        }
                        if (ret)
                        {
                            ((Label)tile[localRow, localCol]).Content = "";
                            if ((int)sd == 1)
                            {
                                GreenPlate.Content = --countGreen;
                            }
                            else if ((int)sd == 0) 
                            {
                                BluePlate.Content = --countGreen;
                            }
                        }
                    }
                    else if (cell[localRow, localCol] == (((int)sd) % 2) + 1)
                    {
                        ret = false;
                        break;
                    }
                    else if (cell[localRow, localCol] == 0)
                    {
                        continue;
                    }
                }
            }
            if (hor[target] < hor[source] && ver[target] > ver[source])//North east 
            {
                for (int m = 1; m <= (hor[source] - hor[target] - 1); m++)
                {
                    int localRow = hor[source] -m;
                    int localCol = ver[source] +m;
                    if (cell[localRow, localCol] == (((int)sd + 1) % 2) + 1) //if another tile
                    {
                        if (ret == false)
                        {
                            break;
                        }
                        for (int n = 1; n <= (row[source] - row[target] - 1 - m); n++)
                        {
                            if (cell[(localRow - n), (n + localCol)] == 0)
                                continue;
                            else
                                ret = false;
                            break;

                        }
                        if (ret)
                        {
                            ((Label)tile[localRow, localCol]).Content = "";
                            cell[localRow, localCol] = 0;
                            if ((int)sd == 1)
                            {
                                GreenPlate.Content = --countGreen;
                            }
                            else if ((int)sd == 0)
                            {
                                BluePlate.Content = --countGreen;
                            }
                        }
                    }
                    else if (cell[localRow, localCol] == (((int)sd) % 2) + 1)
                    {
                        ret = false;
                        break;
                    }
                    else if (cell[localRow, localCol] == 0)
                    {
                        continue;
                    }
                }
            }
            if (hor[target] < hor[source] && ver[target] < ver[source])//North west
            {
                for (int m = 1; m <= (hor[source] - hor[target] - 1); m++)
                {
                    int localRow = hor[source] - m;
                    int localCol = ver[source] - m;
                    if (cell[localRow, localCol] == (((int)sd + 1) % 2) + 1) //if another tile
                    {
                        if (ret == false)
                        {
                            break;
                        }
                        for (int n = 1; n <= (row[source] - row[target] - 1 - m); n++)
                        {
                            if (cell[(localRow - n), (localCol - n)] == 0)
                                continue;
                            else
                                ret = false;
                            break;

                        }
                        if (ret)
                        {
                            ((Label)tile[localRow, localCol]).Content = "";
                            cell[localRow, localCol] = 0;
                            if ((int)sd == 1)
                            {
                                GreenPlate.Content = --countGreen;
                            }
                            else if ((int)sd == 0)
                            {
                                BluePlate.Content = --countGreen;
                            }
                        }
                    }
                    else if (cell[localRow, localCol] == (((int)sd) % 2) + 1)
                    {
                        ret = false;
                        break;
                    }
                    else if (cell[localRow, localCol] == 0)
                    {
                        continue;
                    }
                }
            }
            if (hor[target] > hor[source] && ver[target] < ver[source])//South west
            {
                for (int m = 1; m <= (hor[target] - hor[source] - 1); m++)
                {
                    int localRow = hor[source] + m;
                    int localCol = ver[source] - m;
                    if (cell[localRow, localCol] == (((int)sd + 1) % 2) + 1) //if another tile
                    {
                        if (ret == false)
                        {
                            break;
                        }
                        for (int n = 1; n <= (row[target] - row[source] - 1 - m); n++)
                        {
                            if (cell[(localRow + n), (localCol - n)] == 0)
                                continue;
                            else
                                ret = false;
                            break;

                        }
                        if (ret)
                        {
                            ((Label)tile[localRow, localCol]).Content = "";
                            cell[localRow, localCol] = 0;
                            if ((int)sd == 1)
                            {
                                GreenPlate.Content = --countGreen;
                            }
                            else if ((int)sd == 0)
                            {
                                BluePlate.Content = --countGreen;
                            }
                        }
                    }
                    else if (cell[localRow, localCol] == (((int)sd) % 2) + 1)
                    {
                        ret = false;
                        break;
                    }
                    else if (cell[localRow, localCol] == 0)
                    {
                        continue;
                    }
                }
            }
            return ret;
        }
        public virtual void Logic(int decider)
        {
            //bool valid;
            for (int i = 0; i < 50; i++)
            {
                if ((Board.Children[i].IsMouseOver && mouseMove)/*||((int)md == 0 && (int)sd == 1)*/)
                {
                    //MessageBox.Show("print :"+md);
                    //if ((int)md == 0 && (int)sd == 1)
                    //{
                    //    index = 32;
                    //    i = 27;
                    //}
                    if (enforce)
                    {
                        if (index != reoccur)
                        {
                            continue;
                        }
                    }
                        if ((king[row[index], column[index]]) && (cell[row[i], column[i]] == 0) && cell[row[index], column[index]] == ((int)sd /1)+1)
                        {

                            if (DefineKing(i, index))
                            {
                                setcolor(index);
                                ((Label)tile[row[i], column[i]]).Content = ((Label)tile[row[index], column[index]]).Content;
                                ((Label)tile[row[index], column[index]]).Content = "";
                                cell[row[index], column[index]] = 0; 
                                cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                king[row[i], column[i]] = true;
                                king[row[index], column[index]] = false;
                                Control();
                                TurnMethod((int)sd);
                                //valid = true;
                            }
                        }
                        ///////////////
                        if (cell[row[index], column[index]] == (((int)sd /1)+1) && cell[row[i], column[i]] == 0)//is target empty
                        {
                            if ((row[i] - row[index] == Math.Pow(-1,(int)sd)) && (Math.Pow(column[i] - column[index], 2) == 1))//is d diff btw rows and column both 1;
                            {
                                //MessageBox.Show("Enforce() is: " + Enforce());
                                if (!Enforce())//check if there should be an enforcement 
                                {
                                    setcolor(index);
                                    ((Label)tile[row[i], column[i]]).Content = ((Label)tile[row[index], column[index]]).Content;
                                    cell[row[index], column[index]] = 0;
                                    cell[row[i], column[i]] = ((int)sd /1)+1;
                                    CheckKing((int)sd, i, index);
                                    Control();
                                    TurnMethod((int)sd);
                                    //valid = true;
                                }
                                else
                                {
                                    //valid = false;
                                    continue;
                                }
                            }
                            #region

                            else if ((Math.Pow(row[index] - row[i], 2) == 4) && (Math.Pow(column[i] - column[index], 2) == 4))//is movement a jump
                            {//thus check for validity of jump

                                bool back = false;
                                bool forward = false;
                                // MessageBox.Show("" + column[i] + "\t" + column[index] + "\n" + row[row[index] + 1] + "\t" + column[column[index] + 1] + "\n" + cell[row[index] + 1, column[index] + 1]);
                                try 
                                {
                                    if(cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1]  == 2 / ((int)sd + 1))
                                    {
                                        forward = true;
                                    }
                                }
                                catch
                                {
                                    forward = false;
                                }
                                try { if (cell[row[index] + (2 * ((int)sd) - 1), column[index] + 1] == 2 / ((int)sd + 1)) { back = true; } }
                                catch 
                                {
                                    back = false;
                                }
                                if ((column[i] > column[index]) &&(back || forward))
                                {
                                    int holder = 0;
                                    object place = null;
                                    bool control = false;
                                    setcolor(index);

                                    if (((int)sd == 1 && row[i] < row[index]) || ((int)sd == 0 && row[i] > row[index]))
                                    {
                                        cell[row[index] - (2 * ((int)sd) - 1), column[index] + 1] = holder;
                                        ((Label)tile[row[index] - (2 * ((int)sd) - 1), column[index] + 1]).Content = place;
                                    }
                                    else if (((int)sd == 1 && row[i] > row[index]) || ((int)sd == 0 && row[i] < row[index]))
                                    {
                                        cell[row[index] + (2 * ((int)sd) - 1), column[index] + 1] = holder;
                                        ((Label)tile[row[index] + (2 * ((int)sd) - 1), column[index] + 1]).Content = place;
                                    }
                                    else
                                    {
                                        //MessageBox.Show("Error");
                                    }
                                    ((Label)tile[row[i], column[i]]).Content = (((Label)tile[row[index], column[index]]).Content);
                                    //MessageBox.Show("index and i is: " + index + " and " + i + "respectively");
                                    //((Label)tile[row[index] - (2*((int)sd)- 1), column[index] + 1]).Content = "";
                                    //place = "";
                                    
                                    cell[row[index], column[index]] = 0;
                                    cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                    holder = 0;
                                    deduct((int)sd);
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
                                        if
                                            (cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && cell[row[i] + (4 * (int)sd - 2), column[i] + 2] == 0)
                                            
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
                                        if ((cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && cell[row[i] - (4 * (int)sd - 2), column[i] - 2] == 0) ||
                                            (cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && cell[row[i] + (4 * (int)sd - 2), column[i] - 2] == 0)
                                            )
                                        {
                                            enforce = true;
                                            reoccur = i;
                                            break;
                                        }
                                        else
                                            enforce = false;
                                    }
                                    catch//acting as catch for both trys;
                                    {
                                        if (!control)
                                        {
                                            //MessageBox.Show("Maya don happen!!! 1");
                                            enforce = false;
                                            ///
                                            CheckKing((int)sd, i, index);
                                            Control();
                                            TurnMethod((int)sd);
                                            continue;
                                        }
                                    }
                                        CheckKing((int)sd, i, index);//put a check b$ control meth for continiuty
                                    Control();
                                    TurnMethod((int)sd);

                                }
                                //MessageBox.Show("row["+index+"] + (int)Math.Pow(-1, "+(int)sd+")" + row[index] +" and "+ (int)Math.Pow(-1, (int)sd));
                                //MessageBox.Show("(column[i] < column[index]) && (cell[row[index] + (int)Math.Pow(-1,(int)sd), column[index] - 1] == 2/((int)sd+1))"+
                                //    (column[i] + "  " + column[index]) + "  " + (cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] + "  " + 2 / ((int)sd + 1))
                                //    );
                                back = false;
                                forward = false;
                                try
                                {
                                    if (cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] == 2 / ((int)sd + 1))
                                    {
                                        forward = true;
                                    }
                                }
                                catch
                                {
                                    forward = false;
                                }
                                try { if (cell[row[index] + (int)Math.Pow(-1, ((int)sd + 1) % 2), column[index] - 1] == 2 / ((int)sd + 1)) { back = true; } }
                                catch
                                {
                                    back = false;
                                }

                                if ((column[i] < column[index]) && (forward || back))
                                {
                                    bool control = false;
                                    setcolor(index);
                                    int holder = 0;
                                    object place = null;
                                    if (((int)sd == 1 && row[i] < row[index]) || ((int)sd == 0 && row[i] > row[index]))
                                    {
                                        cell[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1] = holder;
                                        ((Label)tile[row[index] + (int)Math.Pow(-1, (int)sd), column[index] - 1]).Content = place;
                                    }
                                    else if (((int)sd == 1 && row[i] > row[index]) || ((int)sd == 0 && row[i] < row[index]))
                                    {
                                        cell[row[index] - (int)Math.Pow(-1, (int)sd), column[index] - 1] = holder;
                                        ((Label)tile[row[index] - (int)Math.Pow(-1, (int)sd), column[index] - 1]).Content = place;
                                    }
                                    else
                                    {
                                        //MessageBox.Show("Error");
                                    }
                                    ((Label)tile[row[i], column[i]]).Content = ((Label)tile[row[index], column[index]]).Content;
                                    //((Label)tile[row[index] + (int)Math.Pow(-1,(int)sd), column[index] - 1]).Content = "";
                                    //MessageBox.Show("index and i is: " + index + " and " + i + "respectively");
                                    //place = "";
                                    cell[row[index], column[index]] = 0;
                                    cell[row[i], column[i]] = ((int)sd / 1) + 1;
                                    //cell[row[index] + (int)Math.Pow(-1,(int)sd), column[index] - 1] = 0;
                                    holder = 0;
                                    deduct((int)sd);
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
                                        if 
                                            (cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] + 1] == 2 / ((int)sd + 1) && cell[row[i] + (4 * (int)sd - 2), column[i] + 2] == 0)
                                            
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
                                        if ((cell[row[i] + (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && cell[row[i] - (4 * (int)sd - 2), column[i] - 2] == 0) ||
                                            (cell[row[i] - (int)Math.Pow(-1, (int)sd), column[i] - 1] == 2 / ((int)sd + 1) && cell[row[i] + (4 * (int)sd - 2), column[i] - 2] == 0)
                                            )
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
                                            CheckKing((int)sd, i, index);
                                            Control();
                                            TurnMethod((int)sd);
                                            continue;
                                        }
                                    }
                                    CheckKing((int)sd, i, index);
                                    Control();
                                    TurnMethod((int)sd);
                                }
                            }
                            #endregion 
                        }


                }
            }
            mouseDown = false;
            mouseMove = false;
            //MessageBox.Show("THIS IS THE PRESENT TURN " + sd);

        }
        public void deduct(int n)
        {
            if ((int)sd == 0)
            {
                BluePlate.Content = --countBlue;
            }
            if ((int)sd == 1)
            {
                GreenPlate.Content = --countGreen;
            }
        }

        public void Button_Click_1(object sender, RoutedEventArgs e)
        {
            //InitializeComponent();
            //SetRowColumn();
            //BluePlate.Content = countBlue;
            //GreenPlate.Content = countGreen;

            countBlue = 0;
            countGreen = 0;
            SetRowColumn();
            BluePlate.Content = countBlue;
            GreenPlate.Content = countGreen;
            set = false;
            ((Rectangle)Turn.Children[1]).Fill = Brushes.Red;
            start = false;
            //Application
        }
        
        public void setcolor(int recent) 
        {
            for (int i = 0; i < 50; i++)
            {
                if (row[i] == column[i])
                {
                    ((Label)tile[row[i], column[i]]).Background = Brushes.Red;
                }
                else 
                {
                    ((Label)tile[row[i], column[i]]).Background = Brushes.Black;
                }
            }
            try
            {
                ((Label)tile[row[recent], column[recent]]).Background = Brushes.BurlyWood;
            }
            catch { }
            
        }

    }

}