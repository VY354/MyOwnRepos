using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace FourierTransformVisualisation
{


    public partial class Form1 : Form
    {
        // events
        public event EventHandler On_Parameter_Change = null;


        // working with waves
        public Graph_maker graph_maker = new Graph_maker(10,3);
        public Wave selected_wave = new Wave();

        int last_wave_index;



        // controlls paremeters
        public List<TrackBar> TrackBar_List = new List<TrackBar>();

        public int base_scale_factor;
        public double base_step_factor;

        public int scale_factor;
        public double step_factor;

        public double prev_step_factor;
        

        public Form1()
        {

            InitializeComponent();

            //this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            last_wave_index = 0;

            base_scale_factor = 1;
            base_step_factor = 0;

            scale_factor = 1;
            step_factor = 0;

            prev_step_factor = step_factor;

            TrackBar_List.Add(this.scale_trackBar);
            TrackBar_List.Add(this.Phi0_trackBar);
            TrackBar_List.Add(this.wave_frequency_trackBar);
            TrackBar_List.Add(this.rotation_frequency_trackBar);  

            foreach (TrackBar trackar in TrackBar_List)
            {
                trackar.Maximum = Convert.ToInt32(Math.Pow(10, base_scale_factor));
                trackar.SmallChange = 1;
            }

            slider_scale_factor_textBox.Text = scale_factor.ToString();
            slider_step_factor_textBox.Text = step_factor.ToString();

            show_combined_checkBox.Checked = true;
            show_separately_checkBox.Checked = false;


            Function_chart.ChartAreas[0].AxisX.Minimum = 0;

            On_Parameter_Change += Redraw_wrapping_graph;

            On_Parameter_Change.Invoke(this, EventArgs.Empty);


        }


        // graph of wrapping total waves around circle
        private void Redraw_wrapping_graph(object sender, EventArgs e)
        {
            // if on second tab add listener to event
            if (Graphs_tabControl.SelectedIndex == 1) On_Parameter_Change += Redraw_Center_of_mass_graph;
            else On_Parameter_Change -= Redraw_Center_of_mass_graph;

            if (graph_maker.Waves_list.Count == 0) return;

            // creating graph data
            graph_maker.Create_Graph();
            graph_maker.Create_Wrapping_Graph();
            graph_maker.calculate_center_of_mass();

            Graph_chart.Series[0].Points.Clear();
            Graph_chart.Series[1].Points.Clear();

            // adding points
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, graph_maker.Angle_step_factor));
            for (int i = 0; i < num_of_divisions; i++)
            {
                Graph_chart.Series[0].Points.AddXY(graph_maker.x_data_wrapped[i], graph_maker.y_data_wrapped[i]);
            }
            Graph_chart.Series[1].Points.AddXY(graph_maker.x_center_of_mass, graph_maker.y_center_of_mass);

            Graph_chart.Update();
        }

        // graph of sum of waves
        private void Redraw_combined_graph(object sender, EventArgs e)
        {
            if (graph_maker.Waves_list.Count == 0) return;

            // create total summed graph
            graph_maker.Create_Graph();

            Function_chart.Series[0].Points.Clear();

            // fill points
            int num_of_divisions = Convert.ToInt32(Math.Pow(10, graph_maker.Angle_step_factor));
            for (int i = 0; i < num_of_divisions; i++)
            {
                Function_chart.Series[0].Points.AddXY(graph_maker.x_data[i], graph_maker.y_data[i]);
            }

            Function_chart.Update();
        }

        private void Redraw_separeted_graphS(object sender, EventArgs e)
        {
            if (graph_maker.Waves_list.Count < 1) return;

            // update series
            for (int i = 1; i < Function_chart.Series.Count; i++)
            {
                if (graph_maker.Waves_list.Count == 0) return;

                Function_chart.Series[i].Points.Clear();

                // fill points
                int num_of_divisions = Convert.ToInt32(Math.Pow(10, graph_maker.Angle_step_factor));
                for (int j = 0; j < num_of_divisions; j++)
                {
                    Function_chart.Series[i].Points.AddXY(graph_maker.x_data[j], graph_maker.Waves_list[i-1].Wave_y_data[j]);
                }

                Function_chart.Update();
            }

        }

        // graph of center of mass
        public void Redraw_Center_of_mass_graph(object sender, EventArgs e)
        {

            // get last point index if thre are points
            int last_point_index = 0;
            if (center_of_mass_chart.Series[0].Points.Count != 0)
                last_point_index = center_of_mass_chart.Series[0].Points.Count - 1;

            double new_rot_freq = graph_maker.Rotation_frequency;

            // get last rotation frequency if there are points
            double last_rot_freq = 0;
            if (center_of_mass_chart.Series[0].Points.Count != 0)
                last_rot_freq = center_of_mass_chart.Series[0].Points[last_point_index].XValue;

            double new_COM = graph_maker.y_center_of_mass;


            // if slider position greater that last value
            if (new_rot_freq > last_rot_freq)
            {
                center_of_mass_chart.Series[0].Points.AddXY(new_rot_freq, new_COM);
                last_point_index++;
            }
            // if slder position lower that last value
            else if (new_rot_freq < last_rot_freq)
            {
                center_of_mass_chart.Series[0].Points.RemoveAt(last_point_index);
                last_point_index--;
            }

            center_of_mass_chart.Update();
        }

        // change type of function
        private void Function_type_comboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            string selected_value = Function_type_comboBox.SelectedItem.ToString();

            if (selected_value == "sin")
            {
                selected_wave.Used_function_delegate = selected_wave.SIN;
                selected_wave.Func_type = "sin";
            }
            else if (selected_value == "cos")
            {
                selected_wave.Used_function_delegate = selected_wave.COS;
                selected_wave.Func_type = "cos";
            }

            // update wave Y value
            selected_wave.calculate_wave_y_data();

            On_Parameter_Change.Invoke(this, EventArgs.Empty);

        }


        private void scale_trackBar_Scroll(object sender, EventArgs e)
        {   

            double scale_val = scale_trackBar.Value * Math.Pow(10, -step_factor);

            selected_wave.Scale = scale_val;
            selected_wave.calculate_wave_y_data();

            scale_textBox.Text = scale_val.ToString();

            On_Parameter_Change.Invoke(this,EventArgs.Empty);
        }

        private void scale_textBox_TextChanged(object sender, EventArgs e)
        {
            if (scale_textBox.Text == "") return;
            double scale_val;

            try
            {
                scale_val = Convert.ToDouble(scale_textBox.Text);
            }
            catch (Exception exep)
            {
                return;
            }

            // out of boundary
            if (scale_val > scale_trackBar.Maximum) return;

            selected_wave.Scale = scale_val;
            selected_wave.calculate_wave_y_data();

            scale_trackBar.Value = Convert.ToInt32(scale_val / Math.Pow(10, -step_factor));
            On_Parameter_Change.Invoke(this, EventArgs.Empty);
        }

        private void Phi0_trackBar_Scroll(object sender, EventArgs e)
        {
            double phi0_val = Phi0_trackBar.Value * Math.Pow(10, -step_factor);

            selected_wave.Phi_0 = phi0_val;
            selected_wave.calculate_wave_y_data();

            Phi0_textBox.Text = phi0_val.ToString();
            On_Parameter_Change.Invoke(this, EventArgs.Empty);
        }

        private void Phi0_textBox_TextChanged(object sender, EventArgs e)
        {
            double phi0_val;

            try
            {
                phi0_val = Convert.ToDouble(Phi0_textBox.Text);
            }
            catch (Exception exep)
            {
                return;
            }

            // out of boundary
            if (phi0_val > Phi0_trackBar.Maximum) return;

            selected_wave.Phi_0 = phi0_val;
            selected_wave.calculate_wave_y_data();

            Phi0_trackBar.Value = Convert.ToInt32(phi0_val / Math.Pow(10, -step_factor));
            On_Parameter_Change.Invoke(this, EventArgs.Empty);

        }

        private void wave_frequency_trackBar_Scroll(object sender, EventArgs e)
        {
            double wave_freq_val = wave_frequency_trackBar.Value * Math.Pow(10, -step_factor);

            selected_wave.Wave_frequency = wave_freq_val;
            wave_frequency_textBox.Text = wave_freq_val.ToString();
            On_Parameter_Change.Invoke(this, EventArgs.Empty);
        }

        private void wave_frequency_textBox_TextChanged(object sender, EventArgs e)
        {
            if (wave_frequency_textBox.Text == "") return;
            double wave_freq_val;

            try
            {
                wave_freq_val = Convert.ToDouble(wave_frequency_textBox.Text);
            }
            catch (Exception exep)
            {
                return;
            }

            // out of boundary
            if (wave_freq_val > wave_frequency_trackBar.Maximum) return;

            selected_wave.Wave_frequency = wave_freq_val;
            selected_wave.calculate_wave_y_data();

            wave_frequency_trackBar.Value = Convert.ToInt32(wave_freq_val / Math.Pow(10, -step_factor));
            On_Parameter_Change.Invoke(this, EventArgs.Empty);
        }

        private void rotation_frequency_trackBar_Scroll(object sender, EventArgs e)
        {
            double rot_freq_val = rotation_frequency_trackBar.Value * Math.Pow(10, -step_factor);

            graph_maker.Rotation_frequency = rot_freq_val;
            selected_wave.calculate_wave_y_data();

            rotation_frequency_textBox.Text = rot_freq_val.ToString();
            On_Parameter_Change.Invoke(this, EventArgs.Empty);
        }

        private void rotation_frequency_textBox_TextChanged(object sender, EventArgs e)
        {
            if (rotation_frequency_textBox.Text == "") return;
            double rot_freq_val;

            try
            {
                rot_freq_val = Convert.ToDouble(rotation_frequency_textBox.Text);
            }
            catch (Exception exep)
            {
                return;
            }

            // out of boundary
            if (rot_freq_val > rotation_frequency_trackBar.Maximum) return;

            graph_maker.Rotation_frequency = rot_freq_val;
            selected_wave.calculate_wave_y_data();

            rotation_frequency_trackBar.Value = Convert.ToInt32(rot_freq_val / Math.Pow(10, -step_factor));
            On_Parameter_Change.Invoke(this, EventArgs.Empty);
        }

        private void slider_scale_factor_textBox_TextChanged(object sender, EventArgs e)
        {
            if (slider_scale_factor_textBox.Text == "") return;

            int i_value = Convert.ToInt32(slider_scale_factor_textBox.Text);
            scale_factor = i_value;

            foreach (TrackBar trackbar in TrackBar_List)
            {
                try
                {
                    trackbar.Maximum = Convert.ToInt32(Math.Pow(10, scale_factor + step_factor));
                }
                catch (Exception excep)
                {
                    return;
                }
            }
        }

        private void slider_step_factor_textBox_TextChanged(object sender, EventArgs e)
        {
            if (slider_step_factor_textBox.Text == "") return;
            int i_value = Convert.ToInt32(slider_step_factor_textBox.Text);
            step_factor = i_value;

            foreach (TrackBar trackbar in TrackBar_List)
            {
                try
                {
                    trackbar.Maximum = Convert.ToInt32(Math.Pow(10, scale_factor + step_factor));
                }
                catch (Exception excep)
                {
                    return;
                }
            }
        }

        private void Functions_listView_SelectedIndexChanged(object sender, EventArgs e)
        {
            // if no selected
            if (Functions_listView.SelectedItems.Count == 0) return;

            ListViewItem slected_item = Functions_listView.SelectedItems[0];

            // pick up selected index
            int selected_index = Convert.ToInt32(slected_item.SubItems[0].Text);

            // get wave of selected index
            selected_wave = graph_maker.Waves_list[selected_index];

            // update controls value to selected wave values
            Function_type_comboBox.SelectedItem = selected_wave.Func_type;
            scale_textBox.Text = selected_wave.Scale.ToString();
            Phi0_textBox.Text = selected_wave.Phi_0.ToString();
            wave_frequency_textBox.Text = selected_wave.Wave_frequency.ToString();


        }

        private void Add_button_Click(object sender, EventArgs e)
        {
            if (Functions_listView.Items.Count == 0) last_wave_index = 0;

            ListViewItem new_wave_item = new ListViewItem($"{last_wave_index}");

            // adding new wave and item
            Functions_listView.Items.Add(new_wave_item);
            graph_maker.add_new_wave(new Wave());


            // create new corresponding series
            int last_series_number = Function_chart.Series.Count();
            Function_chart.Series.Add("Series " + $"{ last_series_number + 1 }");
            Function_chart.Series[last_series_number].ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            Function_chart.Series[last_series_number].BorderWidth = 3;

            last_wave_index++;

            On_Parameter_Change.Invoke(this, EventArgs.Empty);
        }

        private void Remove_button_Click(object sender, EventArgs e)
        {
            if (Functions_listView.SelectedItems.Count != 0)
            {
                // getting index of wave to remove
                ListViewItem item_to_remove = Functions_listView.SelectedItems[0];
                int removed_index = Convert.ToInt32(item_to_remove.SubItems[0].Text);

                //all items after deleted moves 1 index up
                for (int i = removed_index; i < Functions_listView.Items.Count; i++)
                {
                    int item_index = Convert.ToInt32(Functions_listView.Items[i].SubItems[0].Text);
                    Functions_listView.Items[i].SubItems[0].Text = (item_index - 1).ToString();
                }

                last_wave_index = Functions_listView.Items.Count - 1;
                
                // delete wave from wave_list
                graph_maker.remove_wave(removed_index);
                Functions_listView.Items.Remove(item_to_remove);

                /*
                 * the FIRST wave in Graph_maker wave_list is sum of all functions
                 * 
                 * if have only one function in list
                 * delete that function
                 * otherwise delete next function
                 */
                if (Function_chart.Series.Count == 1) Function_chart.Series.RemoveAt(removed_index);
                else Function_chart.Series.RemoveAt(removed_index + 1);

                Function_chart.Update();

                On_Parameter_Change.Invoke(this, EventArgs.Empty);
            }
        }

        private void show_combined_checkBox_CheckedChanged(object sender, EventArgs e)
        {
            if (show_combined_checkBox.Checked)
            {
                On_Parameter_Change += Redraw_combined_graph;
                On_Parameter_Change.Invoke(this, EventArgs.Empty);
            }
            else
            {
                On_Parameter_Change -= Redraw_combined_graph;

                Function_chart.Series[0].Points.Clear();
                Function_chart.Update();
            }
        }

        private void show_separately_checkBox_CheckedChanged(object sender, EventArgs e)
        {
            if (show_separately_checkBox.Checked)
            {
                On_Parameter_Change += Redraw_separeted_graphS;
                On_Parameter_Change.Invoke(this, EventArgs.Empty);
            }
            else
            {
                On_Parameter_Change -= Redraw_separeted_graphS;

                // clear all series for separeted functions
                for (int i = 1; i < Function_chart.Series.Count; i++)
                    Function_chart.Series[i].Points.Clear();

                Function_chart.Update();
            }
        }

    }


}
