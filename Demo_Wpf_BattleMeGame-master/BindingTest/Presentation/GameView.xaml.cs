﻿using System;
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
using System.Windows.Shapes;

namespace BindingTest.Presentation
{
    /// <summary>
    /// Interaction logic for GameView.xaml
    /// </summary>
    public partial class GameView : Window
    {
        GameViewModel _gameViewModel;

        public GameView()
        {
            _gameViewModel = new GameViewModel();

            DataContext = _gameViewModel;

            InitializeComponent();
        }

        private void ButtonAttack_Click(object sender, RoutedEventArgs e)
        {
            _gameViewModel.CalculateAttackResults();
        }
    }
}
