
namespace FourierTransformVisualisation
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea4 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series5 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.Series series6 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea5 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series7 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea6 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series8 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.scale_label = new System.Windows.Forms.Label();
            this.rotation_frequency_label = new System.Windows.Forms.Label();
            this.scale_trackBar = new System.Windows.Forms.TrackBar();
            this.scale_textBox = new System.Windows.Forms.TextBox();
            this.rotation_frequency_textBox = new System.Windows.Forms.TextBox();
            this.rotation_frequency_trackBar = new System.Windows.Forms.TrackBar();
            this.Main_wave_prameters_groupBox = new System.Windows.Forms.GroupBox();
            this.Function_type_comboBox = new System.Windows.Forms.ComboBox();
            this.Phi0_label = new System.Windows.Forms.Label();
            this.Phi0_trackBar = new System.Windows.Forms.TrackBar();
            this.Phi0_textBox = new System.Windows.Forms.TextBox();
            this.wave_frequency_label = new System.Windows.Forms.Label();
            this.wave_frequency_trackBar = new System.Windows.Forms.TrackBar();
            this.wave_frequency_textBox = new System.Windows.Forms.TextBox();
            this.slider_scale_factor_textBox = new System.Windows.Forms.TextBox();
            this.slider_scale_factor_label = new System.Windows.Forms.Label();
            this.slider_step_factor_textBox = new System.Windows.Forms.TextBox();
            this.slider_step_factor_label = new System.Windows.Forms.Label();
            this.Wrapping_parameters_groupBox = new System.Windows.Forms.GroupBox();
            this.Slider_scale_factors_groupBox = new System.Windows.Forms.GroupBox();
            this.Graph_chart = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.Graph_groupBox = new System.Windows.Forms.GroupBox();
            this.Functions_listView = new System.Windows.Forms.ListView();
            this.function_number_columnHeader = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.Functions_list_groupBox = new System.Windows.Forms.GroupBox();
            this.Remove_button = new System.Windows.Forms.Button();
            this.Add_button = new System.Windows.Forms.Button();
            this.Function_chart = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.show_separately_checkBox = new System.Windows.Forms.CheckBox();
            this.show_combined_checkBox = new System.Windows.Forms.CheckBox();
            this.Graphs_tabControl = new System.Windows.Forms.TabControl();
            this.Functions_graph_tabPage = new System.Windows.Forms.TabPage();
            this.Center_of_mass_graph_tabPage = new System.Windows.Forms.TabPage();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.center_of_mass_chart = new System.Windows.Forms.DataVisualization.Charting.Chart();
            ((System.ComponentModel.ISupportInitialize)(this.scale_trackBar)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.rotation_frequency_trackBar)).BeginInit();
            this.Main_wave_prameters_groupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Phi0_trackBar)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.wave_frequency_trackBar)).BeginInit();
            this.Wrapping_parameters_groupBox.SuspendLayout();
            this.Slider_scale_factors_groupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Graph_chart)).BeginInit();
            this.Graph_groupBox.SuspendLayout();
            this.Functions_list_groupBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Function_chart)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.Graphs_tabControl.SuspendLayout();
            this.Functions_graph_tabPage.SuspendLayout();
            this.Center_of_mass_graph_tabPage.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.center_of_mass_chart)).BeginInit();
            this.SuspendLayout();
            // 
            // scale_label
            // 
            this.scale_label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.scale_label.AutoSize = true;
            this.scale_label.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.scale_label.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.scale_label.Location = new System.Drawing.Point(501, 99);
            this.scale_label.Name = "scale_label";
            this.scale_label.Size = new System.Drawing.Size(61, 26);
            this.scale_label.TabIndex = 0;
            this.scale_label.Text = "scale";
            // 
            // rotation_frequency_label
            // 
            this.rotation_frequency_label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.rotation_frequency_label.AutoSize = true;
            this.rotation_frequency_label.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.rotation_frequency_label.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.rotation_frequency_label.Location = new System.Drawing.Point(367, 44);
            this.rotation_frequency_label.Name = "rotation_frequency_label";
            this.rotation_frequency_label.Size = new System.Drawing.Size(196, 26);
            this.rotation_frequency_label.TabIndex = 4;
            this.rotation_frequency_label.Text = "rotation frequency";
            this.rotation_frequency_label.UseMnemonic = false;
            // 
            // scale_trackBar
            // 
            this.scale_trackBar.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.scale_trackBar.BackColor = System.Drawing.Color.White;
            this.scale_trackBar.Cursor = System.Windows.Forms.Cursors.SizeWE;
            this.scale_trackBar.Location = new System.Drawing.Point(143, 97);
            this.scale_trackBar.Maximum = 1;
            this.scale_trackBar.Name = "scale_trackBar";
            this.scale_trackBar.Size = new System.Drawing.Size(232, 45);
            this.scale_trackBar.TabIndex = 5;
            this.scale_trackBar.TickFrequency = 0;
            this.scale_trackBar.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.scale_trackBar.Scroll += new System.EventHandler(this.scale_trackBar_Scroll);
            // 
            // scale_textBox
            // 
            this.scale_textBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.scale_textBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.scale_textBox.Location = new System.Drawing.Point(37, 97);
            this.scale_textBox.Name = "scale_textBox";
            this.scale_textBox.Size = new System.Drawing.Size(100, 33);
            this.scale_textBox.TabIndex = 6;
            this.scale_textBox.TextChanged += new System.EventHandler(this.scale_textBox_TextChanged);
            // 
            // rotation_frequency_textBox
            // 
            this.rotation_frequency_textBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.rotation_frequency_textBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.rotation_frequency_textBox.Location = new System.Drawing.Point(37, 42);
            this.rotation_frequency_textBox.Name = "rotation_frequency_textBox";
            this.rotation_frequency_textBox.Size = new System.Drawing.Size(100, 33);
            this.rotation_frequency_textBox.TabIndex = 12;
            this.rotation_frequency_textBox.TextChanged += new System.EventHandler(this.rotation_frequency_textBox_TextChanged);
            // 
            // rotation_frequency_trackBar
            // 
            this.rotation_frequency_trackBar.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.rotation_frequency_trackBar.BackColor = System.Drawing.Color.White;
            this.rotation_frequency_trackBar.Cursor = System.Windows.Forms.Cursors.SizeWE;
            this.rotation_frequency_trackBar.Location = new System.Drawing.Point(143, 42);
            this.rotation_frequency_trackBar.Maximum = 1;
            this.rotation_frequency_trackBar.Name = "rotation_frequency_trackBar";
            this.rotation_frequency_trackBar.Size = new System.Drawing.Size(232, 45);
            this.rotation_frequency_trackBar.TabIndex = 11;
            this.rotation_frequency_trackBar.TickFrequency = 0;
            this.rotation_frequency_trackBar.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.rotation_frequency_trackBar.Scroll += new System.EventHandler(this.rotation_frequency_trackBar_Scroll);
            // 
            // Main_wave_prameters_groupBox
            // 
            this.Main_wave_prameters_groupBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.Main_wave_prameters_groupBox.BackColor = System.Drawing.Color.Transparent;
            this.Main_wave_prameters_groupBox.Controls.Add(this.Function_type_comboBox);
            this.Main_wave_prameters_groupBox.Controls.Add(this.Phi0_label);
            this.Main_wave_prameters_groupBox.Controls.Add(this.Phi0_trackBar);
            this.Main_wave_prameters_groupBox.Controls.Add(this.Phi0_textBox);
            this.Main_wave_prameters_groupBox.Controls.Add(this.wave_frequency_label);
            this.Main_wave_prameters_groupBox.Controls.Add(this.scale_label);
            this.Main_wave_prameters_groupBox.Controls.Add(this.wave_frequency_trackBar);
            this.Main_wave_prameters_groupBox.Controls.Add(this.wave_frequency_textBox);
            this.Main_wave_prameters_groupBox.Controls.Add(this.scale_trackBar);
            this.Main_wave_prameters_groupBox.Controls.Add(this.scale_textBox);
            this.Main_wave_prameters_groupBox.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.Main_wave_prameters_groupBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.Main_wave_prameters_groupBox.ForeColor = System.Drawing.Color.Silver;
            this.Main_wave_prameters_groupBox.Location = new System.Drawing.Point(299, 12);
            this.Main_wave_prameters_groupBox.Name = "Main_wave_prameters_groupBox";
            this.Main_wave_prameters_groupBox.Size = new System.Drawing.Size(572, 260);
            this.Main_wave_prameters_groupBox.TabIndex = 13;
            this.Main_wave_prameters_groupBox.TabStop = false;
            this.Main_wave_prameters_groupBox.Text = "Wave parameters";
            // 
            // Function_type_comboBox
            // 
            this.Function_type_comboBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(240)))), ((int)(((byte)(240)))), ((int)(((byte)(240)))));
            this.Function_type_comboBox.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.Function_type_comboBox.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.Function_type_comboBox.FormattingEnabled = true;
            this.Function_type_comboBox.Items.AddRange(new object[] {
            "sin",
            "cos"});
            this.Function_type_comboBox.Location = new System.Drawing.Point(37, 46);
            this.Function_type_comboBox.Name = "Function_type_comboBox";
            this.Function_type_comboBox.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.Function_type_comboBox.Size = new System.Drawing.Size(166, 34);
            this.Function_type_comboBox.TabIndex = 19;
            this.Function_type_comboBox.Text = "sin";
            this.Function_type_comboBox.SelectedIndexChanged += new System.EventHandler(this.Function_type_comboBox_SelectedIndexChanged);
            // 
            // Phi0_label
            // 
            this.Phi0_label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.Phi0_label.AutoSize = true;
            this.Phi0_label.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.Phi0_label.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.Phi0_label.Location = new System.Drawing.Point(501, 148);
            this.Phi0_label.Name = "Phi0_label";
            this.Phi0_label.Size = new System.Drawing.Size(62, 26);
            this.Phi0_label.TabIndex = 16;
            this.Phi0_label.Text = "Phi 0";
            // 
            // Phi0_trackBar
            // 
            this.Phi0_trackBar.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.Phi0_trackBar.BackColor = System.Drawing.Color.White;
            this.Phi0_trackBar.Cursor = System.Windows.Forms.Cursors.SizeWE;
            this.Phi0_trackBar.Location = new System.Drawing.Point(143, 146);
            this.Phi0_trackBar.Maximum = 1;
            this.Phi0_trackBar.Name = "Phi0_trackBar";
            this.Phi0_trackBar.Size = new System.Drawing.Size(232, 45);
            this.Phi0_trackBar.TabIndex = 17;
            this.Phi0_trackBar.TickFrequency = 0;
            this.Phi0_trackBar.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.Phi0_trackBar.Scroll += new System.EventHandler(this.Phi0_trackBar_Scroll);
            // 
            // Phi0_textBox
            // 
            this.Phi0_textBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.Phi0_textBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.Phi0_textBox.Location = new System.Drawing.Point(37, 146);
            this.Phi0_textBox.Name = "Phi0_textBox";
            this.Phi0_textBox.Size = new System.Drawing.Size(100, 33);
            this.Phi0_textBox.TabIndex = 18;
            this.Phi0_textBox.TextChanged += new System.EventHandler(this.Phi0_textBox_TextChanged);
            // 
            // wave_frequency_label
            // 
            this.wave_frequency_label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.wave_frequency_label.AutoSize = true;
            this.wave_frequency_label.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.wave_frequency_label.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.wave_frequency_label.Location = new System.Drawing.Point(393, 201);
            this.wave_frequency_label.Name = "wave_frequency_label";
            this.wave_frequency_label.Size = new System.Drawing.Size(170, 26);
            this.wave_frequency_label.TabIndex = 13;
            this.wave_frequency_label.Text = "wave frequency";
            this.wave_frequency_label.UseMnemonic = false;
            // 
            // wave_frequency_trackBar
            // 
            this.wave_frequency_trackBar.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.wave_frequency_trackBar.BackColor = System.Drawing.Color.White;
            this.wave_frequency_trackBar.Cursor = System.Windows.Forms.Cursors.SizeWE;
            this.wave_frequency_trackBar.Location = new System.Drawing.Point(143, 199);
            this.wave_frequency_trackBar.Maximum = 1;
            this.wave_frequency_trackBar.Name = "wave_frequency_trackBar";
            this.wave_frequency_trackBar.Size = new System.Drawing.Size(232, 45);
            this.wave_frequency_trackBar.TabIndex = 14;
            this.wave_frequency_trackBar.TickFrequency = 0;
            this.wave_frequency_trackBar.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.wave_frequency_trackBar.Scroll += new System.EventHandler(this.wave_frequency_trackBar_Scroll);
            // 
            // wave_frequency_textBox
            // 
            this.wave_frequency_textBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.wave_frequency_textBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.wave_frequency_textBox.Location = new System.Drawing.Point(37, 199);
            this.wave_frequency_textBox.Name = "wave_frequency_textBox";
            this.wave_frequency_textBox.Size = new System.Drawing.Size(100, 33);
            this.wave_frequency_textBox.TabIndex = 15;
            this.wave_frequency_textBox.TextChanged += new System.EventHandler(this.wave_frequency_textBox_TextChanged);
            // 
            // slider_scale_factor_textBox
            // 
            this.slider_scale_factor_textBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.slider_scale_factor_textBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.slider_scale_factor_textBox.Location = new System.Drawing.Point(37, 42);
            this.slider_scale_factor_textBox.Name = "slider_scale_factor_textBox";
            this.slider_scale_factor_textBox.Size = new System.Drawing.Size(100, 33);
            this.slider_scale_factor_textBox.TabIndex = 16;
            this.slider_scale_factor_textBox.TextChanged += new System.EventHandler(this.slider_scale_factor_textBox_TextChanged);
            // 
            // slider_scale_factor_label
            // 
            this.slider_scale_factor_label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.slider_scale_factor_label.AutoSize = true;
            this.slider_scale_factor_label.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.slider_scale_factor_label.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.slider_scale_factor_label.Location = new System.Drawing.Point(300, 44);
            this.slider_scale_factor_label.Name = "slider_scale_factor_label";
            this.slider_scale_factor_label.Size = new System.Drawing.Size(262, 26);
            this.slider_scale_factor_label.TabIndex = 14;
            this.slider_scale_factor_label.Text = "slider scale factor ( 10 ^ n )";
            this.slider_scale_factor_label.UseMnemonic = false;
            // 
            // slider_step_factor_textBox
            // 
            this.slider_step_factor_textBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.slider_step_factor_textBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.slider_step_factor_textBox.Location = new System.Drawing.Point(37, 94);
            this.slider_step_factor_textBox.Name = "slider_step_factor_textBox";
            this.slider_step_factor_textBox.Size = new System.Drawing.Size(100, 33);
            this.slider_step_factor_textBox.TabIndex = 19;
            this.slider_step_factor_textBox.TextChanged += new System.EventHandler(this.slider_step_factor_textBox_TextChanged);
            // 
            // slider_step_factor_label
            // 
            this.slider_step_factor_label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.slider_step_factor_label.AutoSize = true;
            this.slider_step_factor_label.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.slider_step_factor_label.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.slider_step_factor_label.Location = new System.Drawing.Point(299, 96);
            this.slider_step_factor_label.Name = "slider_step_factor_label";
            this.slider_step_factor_label.Size = new System.Drawing.Size(263, 26);
            this.slider_step_factor_label.TabIndex = 17;
            this.slider_step_factor_label.Text = "slider step factor ( 10 ^ -n )";
            this.slider_step_factor_label.UseMnemonic = false;
            // 
            // Wrapping_parameters_groupBox
            // 
            this.Wrapping_parameters_groupBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.Wrapping_parameters_groupBox.Controls.Add(this.rotation_frequency_label);
            this.Wrapping_parameters_groupBox.Controls.Add(this.rotation_frequency_trackBar);
            this.Wrapping_parameters_groupBox.Controls.Add(this.rotation_frequency_textBox);
            this.Wrapping_parameters_groupBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.Wrapping_parameters_groupBox.ForeColor = System.Drawing.Color.Silver;
            this.Wrapping_parameters_groupBox.Location = new System.Drawing.Point(299, 319);
            this.Wrapping_parameters_groupBox.Name = "Wrapping_parameters_groupBox";
            this.Wrapping_parameters_groupBox.Size = new System.Drawing.Size(572, 98);
            this.Wrapping_parameters_groupBox.TabIndex = 20;
            this.Wrapping_parameters_groupBox.TabStop = false;
            this.Wrapping_parameters_groupBox.Text = "Wrapping parameters";
            // 
            // Slider_scale_factors_groupBox
            // 
            this.Slider_scale_factors_groupBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.Slider_scale_factors_groupBox.Controls.Add(this.slider_scale_factor_textBox);
            this.Slider_scale_factors_groupBox.Controls.Add(this.slider_scale_factor_label);
            this.Slider_scale_factors_groupBox.Controls.Add(this.slider_step_factor_textBox);
            this.Slider_scale_factors_groupBox.Controls.Add(this.slider_step_factor_label);
            this.Slider_scale_factors_groupBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.Slider_scale_factors_groupBox.ForeColor = System.Drawing.Color.Silver;
            this.Slider_scale_factors_groupBox.Location = new System.Drawing.Point(299, 458);
            this.Slider_scale_factors_groupBox.Name = "Slider_scale_factors_groupBox";
            this.Slider_scale_factors_groupBox.Size = new System.Drawing.Size(572, 147);
            this.Slider_scale_factors_groupBox.TabIndex = 21;
            this.Slider_scale_factors_groupBox.TabStop = false;
            this.Slider_scale_factors_groupBox.Text = "Slider scale and step factors";
            // 
            // Graph_chart
            // 
            this.Graph_chart.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.Graph_chart.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None;
            chartArea4.AxisX.LabelStyle.Enabled = false;
            chartArea4.AxisX.LineColor = System.Drawing.Color.Transparent;
            chartArea4.AxisX.LineWidth = 2;
            chartArea4.AxisX.MajorGrid.Enabled = false;
            chartArea4.AxisX.MajorTickMark.Enabled = false;
            chartArea4.AxisX.TitleFont = new System.Drawing.Font("Montserrat Medium", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea4.AxisX.TitleForeColor = System.Drawing.Color.Transparent;
            chartArea4.AxisX2.MajorGrid.Enabled = false;
            chartArea4.AxisX2.TitleFont = new System.Drawing.Font("Montserrat", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea4.AxisY.LabelStyle.Enabled = false;
            chartArea4.AxisY.LineColor = System.Drawing.Color.Transparent;
            chartArea4.AxisY.LineWidth = 2;
            chartArea4.AxisY.MajorGrid.Enabled = false;
            chartArea4.AxisY.MajorTickMark.Enabled = false;
            chartArea4.AxisY.TitleFont = new System.Drawing.Font("Montserrat", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            chartArea4.AxisY.TitleForeColor = System.Drawing.Color.Transparent;
            chartArea4.AxisY2.MajorGrid.Enabled = false;
            chartArea4.AxisY2.TitleFont = new System.Drawing.Font("Montserrat", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea4.AxisY2.TitleForeColor = System.Drawing.Color.Transparent;
            chartArea4.Name = "ChartArea1";
            chartArea4.ShadowColor = System.Drawing.Color.Transparent;
            this.Graph_chart.ChartAreas.Add(chartArea4);
            this.Graph_chart.Location = new System.Drawing.Point(6, 32);
            this.Graph_chart.Name = "Graph_chart";
            this.Graph_chart.Palette = System.Windows.Forms.DataVisualization.Charting.ChartColorPalette.Bright;
            series5.BorderWidth = 3;
            series5.ChartArea = "ChartArea1";
            series5.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series5.Color = System.Drawing.Color.DodgerBlue;
            series5.CustomProperties = "IsXAxisQuantitative=True";
            series5.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            series5.Name = "Series1";
            series5.ShadowColor = System.Drawing.Color.White;
            series6.ChartArea = "ChartArea1";
            series6.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Point;
            series6.LabelBorderWidth = 5;
            series6.MarkerBorderColor = System.Drawing.Color.Red;
            series6.MarkerColor = System.Drawing.Color.Red;
            series6.MarkerSize = 15;
            series6.MarkerStyle = System.Windows.Forms.DataVisualization.Charting.MarkerStyle.Circle;
            series6.Name = "Series2";
            this.Graph_chart.Series.Add(series5);
            this.Graph_chart.Series.Add(series6);
            this.Graph_chart.Size = new System.Drawing.Size(583, 555);
            this.Graph_chart.TabIndex = 22;
            this.Graph_chart.Text = "Graph";
            // 
            // Graph_groupBox
            // 
            this.Graph_groupBox.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.Graph_groupBox.BackColor = System.Drawing.Color.White;
            this.Graph_groupBox.Controls.Add(this.Graph_chart);
            this.Graph_groupBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.Graph_groupBox.ForeColor = System.Drawing.Color.Silver;
            this.Graph_groupBox.Location = new System.Drawing.Point(877, 12);
            this.Graph_groupBox.Name = "Graph_groupBox";
            this.Graph_groupBox.Size = new System.Drawing.Size(595, 593);
            this.Graph_groupBox.TabIndex = 23;
            this.Graph_groupBox.TabStop = false;
            this.Graph_groupBox.Text = "Wrapping graph";
            // 
            // Functions_listView
            // 
            this.Functions_listView.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.Functions_listView.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.function_number_columnHeader});
            this.Functions_listView.FullRowSelect = true;
            this.Functions_listView.GridLines = true;
            this.Functions_listView.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
            this.Functions_listView.HideSelection = false;
            this.Functions_listView.Location = new System.Drawing.Point(6, 32);
            this.Functions_listView.Name = "Functions_listView";
            this.Functions_listView.Size = new System.Drawing.Size(269, 452);
            this.Functions_listView.TabIndex = 24;
            this.Functions_listView.UseCompatibleStateImageBehavior = false;
            this.Functions_listView.View = System.Windows.Forms.View.Details;
            this.Functions_listView.SelectedIndexChanged += new System.EventHandler(this.Functions_listView_SelectedIndexChanged);
            // 
            // function_number_columnHeader
            // 
            this.function_number_columnHeader.Text = "Function number";
            this.function_number_columnHeader.Width = 268;
            // 
            // Functions_list_groupBox
            // 
            this.Functions_list_groupBox.Controls.Add(this.Functions_listView);
            this.Functions_list_groupBox.Controls.Add(this.Remove_button);
            this.Functions_list_groupBox.Controls.Add(this.Add_button);
            this.Functions_list_groupBox.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.Functions_list_groupBox.ForeColor = System.Drawing.Color.Silver;
            this.Functions_list_groupBox.Location = new System.Drawing.Point(12, 12);
            this.Functions_list_groupBox.Name = "Functions_list_groupBox";
            this.Functions_list_groupBox.Size = new System.Drawing.Size(281, 593);
            this.Functions_list_groupBox.TabIndex = 25;
            this.Functions_list_groupBox.TabStop = false;
            this.Functions_list_groupBox.Text = "Functions list";
            // 
            // Remove_button
            // 
            this.Remove_button.FlatAppearance.BorderColor = System.Drawing.Color.Silver;
            this.Remove_button.FlatAppearance.BorderSize = 2;
            this.Remove_button.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.Remove_button.Font = new System.Drawing.Font("Montserrat Medium", 16F);
            this.Remove_button.ForeColor = System.Drawing.Color.Gray;
            this.Remove_button.Location = new System.Drawing.Point(150, 503);
            this.Remove_button.Name = "Remove_button";
            this.Remove_button.Size = new System.Drawing.Size(125, 63);
            this.Remove_button.TabIndex = 26;
            this.Remove_button.Text = "Remove";
            this.Remove_button.UseVisualStyleBackColor = true;
            this.Remove_button.Click += new System.EventHandler(this.Remove_button_Click);
            // 
            // Add_button
            // 
            this.Add_button.FlatAppearance.BorderColor = System.Drawing.Color.Silver;
            this.Add_button.FlatAppearance.BorderSize = 2;
            this.Add_button.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.Add_button.Font = new System.Drawing.Font("Montserrat Medium", 16F);
            this.Add_button.ForeColor = System.Drawing.Color.Gray;
            this.Add_button.Location = new System.Drawing.Point(6, 503);
            this.Add_button.Name = "Add_button";
            this.Add_button.Size = new System.Drawing.Size(125, 63);
            this.Add_button.TabIndex = 25;
            this.Add_button.Text = "Add";
            this.Add_button.UseVisualStyleBackColor = true;
            this.Add_button.Click += new System.EventHandler(this.Add_button_Click);
            // 
            // Function_chart
            // 
            this.Function_chart.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            chartArea5.AxisX.Interval = 3.14D;
            chartArea5.AxisX.IsLabelAutoFit = false;
            chartArea5.AxisX.LabelStyle.Font = new System.Drawing.Font("Montserrat", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea5.AxisX.LabelStyle.ForeColor = System.Drawing.Color.Gray;
            chartArea5.AxisX.LabelStyle.Format = "0.00";
            chartArea5.AxisX.LabelStyle.Interval = 6.28D;
            chartArea5.AxisX.LabelStyle.IntervalOffset = 0D;
            chartArea5.AxisX.LabelStyle.IntervalOffsetType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea5.AxisX.LabelStyle.IntervalType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea5.AxisX.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisX.LineWidth = 2;
            chartArea5.AxisX.MajorGrid.Interval = 6.28D;
            chartArea5.AxisX.MajorGrid.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisX.MajorGrid.LineWidth = 3;
            chartArea5.AxisX.MajorTickMark.Interval = 3.14D;
            chartArea5.AxisX.MajorTickMark.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisX.MajorTickMark.LineWidth = 2;
            chartArea5.AxisX.MinorGrid.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisX.MinorGrid.LineWidth = 2;
            chartArea5.AxisX.TitleFont = new System.Drawing.Font("Montserrat", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            chartArea5.AxisX.TitleForeColor = System.Drawing.Color.Gray;
            chartArea5.AxisX2.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisX2.LineWidth = 2;
            chartArea5.AxisX2.MajorGrid.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisX2.MajorGrid.LineWidth = 2;
            chartArea5.AxisX2.MajorTickMark.LineColor = System.Drawing.Color.Silver;
            chartArea5.AxisX2.MajorTickMark.LineWidth = 2;
            chartArea5.AxisX2.MajorTickMark.Size = 2F;
            chartArea5.AxisX2.MinorGrid.Enabled = true;
            chartArea5.AxisX2.MinorGrid.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisX2.MinorGrid.LineWidth = 2;
            chartArea5.AxisX2.TitleFont = new System.Drawing.Font("Montserrat Medium", 11F);
            chartArea5.AxisX2.TitleForeColor = System.Drawing.Color.Gray;
            chartArea5.AxisY.IsLabelAutoFit = false;
            chartArea5.AxisY.LabelStyle.Enabled = false;
            chartArea5.AxisY.LabelStyle.Font = new System.Drawing.Font("Montserrat", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea5.AxisY.LabelStyle.ForeColor = System.Drawing.Color.Gray;
            chartArea5.AxisY.LineColor = System.Drawing.Color.Gray;
            chartArea5.AxisY.LineWidth = 3;
            chartArea5.AxisY.MajorGrid.Enabled = false;
            chartArea5.AxisY.MajorGrid.LineColor = System.Drawing.Color.Silver;
            chartArea5.AxisY.MajorGrid.LineWidth = 2;
            chartArea5.AxisY.MajorTickMark.Enabled = false;
            chartArea5.AxisY.MinorGrid.LineColor = System.Drawing.Color.Silver;
            chartArea5.AxisY.MinorGrid.LineWidth = 2;
            chartArea5.AxisY2.MajorGrid.LineColor = System.Drawing.Color.Silver;
            chartArea5.AxisY2.MajorGrid.LineWidth = 2;
            chartArea5.AxisY2.MajorTickMark.Enabled = false;
            chartArea5.AxisY2.MajorTickMark.LineColor = System.Drawing.Color.Silver;
            chartArea5.AxisY2.MajorTickMark.LineWidth = 2;
            chartArea5.AxisY2.MajorTickMark.Size = 2F;
            chartArea5.AxisY2.TitleFont = new System.Drawing.Font("Montserrat Medium", 14F);
            chartArea5.AxisY2.TitleForeColor = System.Drawing.Color.Gray;
            chartArea5.BorderColor = System.Drawing.Color.Transparent;
            chartArea5.Name = "ChartArea1";
            chartArea5.ShadowColor = System.Drawing.Color.Transparent;
            this.Function_chart.ChartAreas.Add(chartArea5);
            this.Function_chart.Location = new System.Drawing.Point(209, 32);
            this.Function_chart.Name = "Function_chart";
            series7.BorderWidth = 3;
            series7.ChartArea = "ChartArea1";
            series7.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series7.Color = System.Drawing.Color.DodgerBlue;
            series7.Name = "Series1";
            this.Function_chart.Series.Add(series7);
            this.Function_chart.Size = new System.Drawing.Size(1225, 334);
            this.Function_chart.TabIndex = 26;
            this.Function_chart.Text = "Function graph";
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.show_separately_checkBox);
            this.groupBox1.Controls.Add(this.show_combined_checkBox);
            this.groupBox1.Controls.Add(this.Function_chart);
            this.groupBox1.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.groupBox1.ForeColor = System.Drawing.Color.Silver;
            this.groupBox1.Location = new System.Drawing.Point(6, 6);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(1440, 372);
            this.groupBox1.TabIndex = 27;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Function graph";
            // 
            // show_separately_checkBox
            // 
            this.show_separately_checkBox.AutoSize = true;
            this.show_separately_checkBox.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.show_separately_checkBox.FlatAppearance.BorderSize = 2;
            this.show_separately_checkBox.FlatAppearance.CheckedBackColor = System.Drawing.Color.Gray;
            this.show_separately_checkBox.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.show_separately_checkBox.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.show_separately_checkBox.Location = new System.Drawing.Point(19, 81);
            this.show_separately_checkBox.Name = "show_separately_checkBox";
            this.show_separately_checkBox.Size = new System.Drawing.Size(186, 30);
            this.show_separately_checkBox.TabIndex = 28;
            this.show_separately_checkBox.Text = "show separately";
            this.show_separately_checkBox.UseVisualStyleBackColor = true;
            this.show_separately_checkBox.CheckedChanged += new System.EventHandler(this.show_separately_checkBox_CheckedChanged);
            // 
            // show_combined_checkBox
            // 
            this.show_combined_checkBox.AutoSize = true;
            this.show_combined_checkBox.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.show_combined_checkBox.FlatAppearance.BorderSize = 2;
            this.show_combined_checkBox.FlatAppearance.CheckedBackColor = System.Drawing.Color.Gray;
            this.show_combined_checkBox.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.show_combined_checkBox.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(64)))), ((int)(((byte)(64)))));
            this.show_combined_checkBox.Location = new System.Drawing.Point(19, 45);
            this.show_combined_checkBox.Name = "show_combined_checkBox";
            this.show_combined_checkBox.Size = new System.Drawing.Size(184, 30);
            this.show_combined_checkBox.TabIndex = 27;
            this.show_combined_checkBox.Text = "show combined";
            this.show_combined_checkBox.UseVisualStyleBackColor = true;
            this.show_combined_checkBox.CheckedChanged += new System.EventHandler(this.show_combined_checkBox_CheckedChanged);
            // 
            // Graphs_tabControl
            // 
            this.Graphs_tabControl.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.Graphs_tabControl.Controls.Add(this.Functions_graph_tabPage);
            this.Graphs_tabControl.Controls.Add(this.Center_of_mass_graph_tabPage);
            this.Graphs_tabControl.Font = new System.Drawing.Font("Montserrat Medium", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.Graphs_tabControl.Location = new System.Drawing.Point(12, 611);
            this.Graphs_tabControl.Name = "Graphs_tabControl";
            this.Graphs_tabControl.SelectedIndex = 0;
            this.Graphs_tabControl.Size = new System.Drawing.Size(1460, 419);
            this.Graphs_tabControl.TabIndex = 28;
            // 
            // Functions_graph_tabPage
            // 
            this.Functions_graph_tabPage.BackColor = System.Drawing.Color.White;
            this.Functions_graph_tabPage.Controls.Add(this.groupBox1);
            this.Functions_graph_tabPage.Font = new System.Drawing.Font("Montserrat Medium", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.Functions_graph_tabPage.ForeColor = System.Drawing.Color.Silver;
            this.Functions_graph_tabPage.Location = new System.Drawing.Point(4, 31);
            this.Functions_graph_tabPage.Name = "Functions_graph_tabPage";
            this.Functions_graph_tabPage.Padding = new System.Windows.Forms.Padding(3);
            this.Functions_graph_tabPage.Size = new System.Drawing.Size(1452, 384);
            this.Functions_graph_tabPage.TabIndex = 0;
            this.Functions_graph_tabPage.Text = "Functions graph";
            // 
            // Center_of_mass_graph_tabPage
            // 
            this.Center_of_mass_graph_tabPage.BackColor = System.Drawing.Color.White;
            this.Center_of_mass_graph_tabPage.Controls.Add(this.groupBox2);
            this.Center_of_mass_graph_tabPage.ForeColor = System.Drawing.Color.Silver;
            this.Center_of_mass_graph_tabPage.Location = new System.Drawing.Point(4, 31);
            this.Center_of_mass_graph_tabPage.Name = "Center_of_mass_graph_tabPage";
            this.Center_of_mass_graph_tabPage.Padding = new System.Windows.Forms.Padding(3);
            this.Center_of_mass_graph_tabPage.Size = new System.Drawing.Size(1452, 384);
            this.Center_of_mass_graph_tabPage.TabIndex = 1;
            this.Center_of_mass_graph_tabPage.Text = "Center of mass graph";
            // 
            // groupBox2
            // 
            this.groupBox2.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox2.Controls.Add(this.center_of_mass_chart);
            this.groupBox2.Font = new System.Drawing.Font("Montserrat Medium", 14F);
            this.groupBox2.ForeColor = System.Drawing.Color.Silver;
            this.groupBox2.Location = new System.Drawing.Point(6, 6);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(1440, 350);
            this.groupBox2.TabIndex = 0;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Center of mass graph";
            // 
            // center_of_mass_chart
            // 
            chartArea6.AxisX.IsLabelAutoFit = false;
            chartArea6.AxisX.LabelStyle.Font = new System.Drawing.Font("Montserrat", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea6.AxisX.LabelStyle.ForeColor = System.Drawing.Color.Gray;
            chartArea6.AxisX.LabelStyle.Format = "0.00";
            chartArea6.AxisX.LabelStyle.Interval = 0.5D;
            chartArea6.AxisX.LabelStyle.IntervalOffsetType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea6.AxisX.LabelStyle.IntervalType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea6.AxisX.LineColor = System.Drawing.Color.Gray;
            chartArea6.AxisX.LineWidth = 3;
            chartArea6.AxisX.MajorGrid.Interval = 0D;
            chartArea6.AxisX.MajorGrid.LineColor = System.Drawing.Color.Gray;
            chartArea6.AxisX.MajorGrid.LineWidth = 3;
            chartArea6.AxisX.MajorTickMark.Enabled = false;
            chartArea6.AxisX.MajorTickMark.Interval = 0D;
            chartArea6.AxisX.MajorTickMark.IntervalType = System.Windows.Forms.DataVisualization.Charting.DateTimeIntervalType.Number;
            chartArea6.AxisX.MinorGrid.Interval = double.NaN;
            chartArea6.AxisX.Title = "Frequency of rotation";
            chartArea6.AxisX.TitleFont = new System.Drawing.Font("Montserrat", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea6.AxisX.TitleForeColor = System.Drawing.Color.Gray;
            chartArea6.AxisY.IsLabelAutoFit = false;
            chartArea6.AxisY.LabelStyle.Enabled = false;
            chartArea6.AxisY.LabelStyle.Font = new System.Drawing.Font("Montserrat", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea6.AxisY.LabelStyle.ForeColor = System.Drawing.Color.Gray;
            chartArea6.AxisY.LineColor = System.Drawing.Color.Gray;
            chartArea6.AxisY.LineWidth = 2;
            chartArea6.AxisY.MajorGrid.Enabled = false;
            chartArea6.AxisY.MajorTickMark.Enabled = false;
            chartArea6.AxisY.Title = "C.O.M. coordinate";
            chartArea6.AxisY.TitleFont = new System.Drawing.Font("Montserrat", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            chartArea6.AxisY.TitleForeColor = System.Drawing.Color.Gray;
            chartArea6.Name = "ChartArea1";
            this.center_of_mass_chart.ChartAreas.Add(chartArea6);
            this.center_of_mass_chart.Location = new System.Drawing.Point(6, 32);
            this.center_of_mass_chart.Name = "center_of_mass_chart";
            series8.BorderWidth = 3;
            series8.ChartArea = "ChartArea1";
            series8.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series8.Color = System.Drawing.Color.DodgerBlue;
            series8.Name = "Series1";
            this.center_of_mass_chart.Series.Add(series8);
            this.center_of_mass_chart.Size = new System.Drawing.Size(1428, 312);
            this.center_of_mass_chart.TabIndex = 0;
            this.center_of_mass_chart.Text = "chart1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1483, 1042);
            this.Controls.Add(this.Graphs_tabControl);
            this.Controls.Add(this.Slider_scale_factors_groupBox);
            this.Controls.Add(this.Main_wave_prameters_groupBox);
            this.Controls.Add(this.Wrapping_parameters_groupBox);
            this.Controls.Add(this.Graph_groupBox);
            this.Controls.Add(this.Functions_list_groupBox);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.scale_trackBar)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.rotation_frequency_trackBar)).EndInit();
            this.Main_wave_prameters_groupBox.ResumeLayout(false);
            this.Main_wave_prameters_groupBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Phi0_trackBar)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.wave_frequency_trackBar)).EndInit();
            this.Wrapping_parameters_groupBox.ResumeLayout(false);
            this.Wrapping_parameters_groupBox.PerformLayout();
            this.Slider_scale_factors_groupBox.ResumeLayout(false);
            this.Slider_scale_factors_groupBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Graph_chart)).EndInit();
            this.Graph_groupBox.ResumeLayout(false);
            this.Functions_list_groupBox.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.Function_chart)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.Graphs_tabControl.ResumeLayout(false);
            this.Functions_graph_tabPage.ResumeLayout(false);
            this.Center_of_mass_graph_tabPage.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.center_of_mass_chart)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label scale_label;
        private System.Windows.Forms.Label rotation_frequency_label;
        private System.Windows.Forms.TrackBar scale_trackBar;
        private System.Windows.Forms.TextBox scale_textBox;
        private System.Windows.Forms.TextBox rotation_frequency_textBox;
        private System.Windows.Forms.TrackBar rotation_frequency_trackBar;
        private System.Windows.Forms.GroupBox Main_wave_prameters_groupBox;
        private System.Windows.Forms.TextBox slider_scale_factor_textBox;
        private System.Windows.Forms.Label slider_scale_factor_label;
        private System.Windows.Forms.TextBox slider_step_factor_textBox;
        private System.Windows.Forms.Label slider_step_factor_label;
        private System.Windows.Forms.GroupBox Wrapping_parameters_groupBox;
        private System.Windows.Forms.GroupBox Slider_scale_factors_groupBox;
        private System.Windows.Forms.DataVisualization.Charting.Chart Graph_chart;
        private System.Windows.Forms.GroupBox Graph_groupBox;
        private System.Windows.Forms.Label wave_frequency_label;
        private System.Windows.Forms.TrackBar wave_frequency_trackBar;
        private System.Windows.Forms.TextBox wave_frequency_textBox;
        private System.Windows.Forms.Label Phi0_label;
        private System.Windows.Forms.TrackBar Phi0_trackBar;
        private System.Windows.Forms.TextBox Phi0_textBox;
        private System.Windows.Forms.ListView Functions_listView;
        private System.Windows.Forms.GroupBox Functions_list_groupBox;
        private System.Windows.Forms.ColumnHeader function_number_columnHeader;
        private System.Windows.Forms.DataVisualization.Charting.Chart Function_chart;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button Remove_button;
        private System.Windows.Forms.Button Add_button;
        private System.Windows.Forms.ComboBox Function_type_comboBox;
        private System.Windows.Forms.CheckBox show_separately_checkBox;
        private System.Windows.Forms.CheckBox show_combined_checkBox;
        private System.Windows.Forms.TabControl Graphs_tabControl;
        private System.Windows.Forms.TabPage Functions_graph_tabPage;
        private System.Windows.Forms.TabPage Center_of_mass_graph_tabPage;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.DataVisualization.Charting.Chart center_of_mass_chart;
    }
}

