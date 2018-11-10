from unittest.mock import patch
from dice import Dice
import pytest

@patch('random.randint')
def test_roll_dice(mock_randint):
    dice = Dice(1, 6)
    dice.roll()
    mock_randint.assert_called_once_with(1, 7) 
    
