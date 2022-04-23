using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FourierTransformVisualisation
{
    public class Wave
    {
        private string func_type;

        public delegate double Used_function(double value);
        public Used_function Used_function_delegate;

        private double scale;
        private double wave_frequency;
        private double phi_0;
        private double max_angle;

        private int angle_step_factor;
        private double[] angles;

        private double[] wave_y_data;

        public string Func_type { get { return func_type; } set { func_type = value; } }
        public double Scale { get { return scale; } set { scale = value; } }
        public double Wave_frequency { get { return wave_frequency; } set { wave_frequency = value; } }
        public double Phi_0 { get { return phi_0; } set { phi_0 = value; } }
        public double Max_angle { get { return max_angle; } set { max_angle = value; } }
        public int Angle_step_factor { get { return angle_step_factor; } set { angle_step_factor = value; } }
        public double[] Angles { get { return angles; } set { angles = value; } }
        public double[] Wave_y_data { get { return wave_y_data; } set { wave_y_data = value; } }

        public Wave()
        {
            func_type = "sin";
            Used_function_delegate = new Used_function(SIN);

            max_angle = 2 * Math.PI;
            angle_step_factor = 3;
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            this.scale = 1;
            this.wave_frequency = 1;
            this.phi_0 = 0;

            double step = max_angle / num_of_divisions;
            angles = new double[num_of_divisions];
            for (int i = 0; i < num_of_divisions; i++)
            {
                angles[i] = i * step;
            }

            wave_y_data = new double[num_of_divisions];


        }

        public Wave(double max_angle, double scale, double wave_frequency, double phi_0)
        {
            func_type = "sin";
            Used_function_delegate = new Used_function(SIN);

            this.max_angle = max_angle * Math.PI;
            angle_step_factor = 3;
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            this.scale = scale;
            this.wave_frequency = wave_frequency;
            this.phi_0 = phi_0;

            double step = this.max_angle / num_of_divisions;
            angles = new double[num_of_divisions];
            for (int i = 0; i < num_of_divisions; i++)
            {
                angles[i] = i * step;
            }

            wave_y_data = new double[num_of_divisions];

        }

        public void calculate_wave_y_data()
        {
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, angle_step_factor));

            double step = this.max_angle / num_of_divisions;
            angles = new double[num_of_divisions];
            for (int i = 0; i < num_of_divisions; i++)
            {
                angles[i] = i * step;
            }

            for (int i = 0; i < num_of_divisions; i++)
            {
                wave_y_data[i] = scale * Used_function_delegate(wave_frequency * angles[i] + phi_0)+1;
            }

        }


        public double SIN(double value)
        {
            return Math.Sin(value);
        }

        public double COS(double value)
        {
            return Math.Cos(value);
        }


    }

}
