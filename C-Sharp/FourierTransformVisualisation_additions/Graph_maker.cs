using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FourierTransformVisualisation
{

    public class Graph_maker
    {
        //events
        public event EventHandler On_max_angle_change = null;

        //anlges parameters
        private double max_angle;
        private int angle_step_factor;
        private double[] angles;

        //wrapping parameters
        private double rotation_frequency;

        private List<Wave> waves_list;

        //graph XY data
        private double[] X_data;
        private double[] Y_data;

        //wrapped graph XY data
        private double[] X_data_wrapped;
        private double[] Y_data_wrapped;

        //other graph parameters
        double X_center_of_mass;
        double Y_center_of_mass;

        public double Rotation_frequency { get { return rotation_frequency; } set { rotation_frequency = value; } }
        public int Angle_step_factor { get { return angle_step_factor; } set { angle_step_factor = value; } }

        public List<Wave> Waves_list { get { return waves_list; } set { waves_list = value; } }

        public double[] x_data { get { return X_data; } set {; } }
        public double[] y_data { get { return Y_data; } set {; } }

        public double[] x_data_wrapped { get { return X_data_wrapped; } set {; } }
        public double[] y_data_wrapped { get { return Y_data_wrapped; } set {; } }

        public double x_center_of_mass { get { return X_center_of_mass; } set { X_center_of_mass = value; } }
        public double y_center_of_mass { get { return Y_center_of_mass; } set { Y_center_of_mass = value; } }

        public Graph_maker()
        {
            max_angle = 2 * Math.PI;
            angle_step_factor = 3;
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            double step = max_angle / num_of_divisions;
            angles = new double[num_of_divisions];
            for (int i = 0; i < num_of_divisions; i++)
            {
                angles[i] = i * step;
            }

            rotation_frequency = 1;

            waves_list = new List<Wave>();

            X_data = angles;
            Y_data = new double[num_of_divisions];

            X_data_wrapped = new double[num_of_divisions];
            Y_data_wrapped = new double[num_of_divisions];

            x_center_of_mass = 0;
            y_center_of_mass = 0;

            On_max_angle_change += RecalculateAngles;

        }

        public Graph_maker(double max_angle, int angle_step_factor=3, double rotation_frequency=1)
        {
            this.max_angle = max_angle * Math.PI;
            this.angle_step_factor = angle_step_factor;
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            double step = this.max_angle / num_of_divisions;
            angles = new double[num_of_divisions];
            for (int i = 0; i < num_of_divisions; i++)
            {
                angles[i] = i * step;
            }

            this.rotation_frequency = rotation_frequency;

            waves_list = new List<Wave>();

            X_data = angles;
            Y_data = new double[num_of_divisions];

            X_data_wrapped = new double[num_of_divisions];
            Y_data_wrapped = new double[num_of_divisions];

            x_center_of_mass = 0;
            y_center_of_mass = 0;

            On_max_angle_change += RecalculateAngles;

        }

        public void add_new_wave(Wave new_wave)
        {
            new_wave.Max_angle = max_angle;
            new_wave.Angle_step_factor = angle_step_factor;
            new_wave.calculate_wave_y_data();

            waves_list.Add(new_wave);
        }

        public void remove_wave(int index)
        {
            waves_list.RemoveAt(index);
        }

        public void Create_Wrapping_Graph()
        {
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            for (int i = 0; i < num_of_divisions; i++)
            {
                double total_y_value = 0;
                for (int j = 0; j < waves_list.Count; j++)
                {
                    total_y_value += waves_list[j].Wave_y_data[i];
                }
                X_data_wrapped[i] = Math.Cos(rotation_frequency * angles[i]) * total_y_value;
                Y_data_wrapped[i] = Math.Sin(rotation_frequency * angles[i]) * total_y_value;
            }
        }

        public void Create_Graph()
        {
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            for (int i = 0; i < num_of_divisions; i++)
            {
                double total_y_value = 0;
                for (int j = 0; j < waves_list.Count; j++)
                {
                    total_y_value += waves_list[j].Wave_y_data[i];
                }
                Y_data[i] = total_y_value;
            }
        }

        public void RecalculateAngles(object sender, EventArgs e)
        {

            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            double step = this.max_angle / num_of_divisions;
            angles = new double[num_of_divisions];
            for (int i = 0; i < num_of_divisions; i++)
            {
                angles[i] = i * step;
            }

            for (int j = 0; j < waves_list.Count; j++)
            {
                waves_list[j].Angles = angles;
            }
        }


        public void calculate_center_of_mass()
        {
            x_center_of_mass = 0;
            y_center_of_mass = 0;

            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            for (int i = 0; i < num_of_divisions; i++)
            {
                x_center_of_mass += X_data_wrapped[i];
                y_center_of_mass += Y_data_wrapped[i];
            }

            x_center_of_mass /= num_of_divisions;
            y_center_of_mass /= num_of_divisions;

        }


    }
}
