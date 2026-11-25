{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM9SJIpbYzVrrQ1zWVP+gKK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ravirajchavan2212/Butterfly-pattern-/blob/main/number_guessing_game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "60NZHRWOkitb",
        "outputId": "914cc563-671b-4227-c63a-3ca5b0474b23"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "================================\n",
            "     NUMBER GUESSING GAME\n",
            "================================\n",
            "Enter your guess (1-100): 4\n",
            "Too low! Try a bigger number.\n",
            "Enter your guess (1-100): 60\n",
            "Too high! Try a smaller number.\n",
            "Enter your guess (1-100): 50\n",
            "Too high! Try a smaller number.\n",
            "Enter your guess (1-100): 40\n",
            "Too high! Try a smaller number.\n",
            "Enter your guess (1-100): 30\n",
            "Too high! Try a smaller number.\n",
            "Enter your guess (1-100): 20\n",
            "Too high! Try a smaller number.\n",
            "Enter your guess (1-100): 10\n",
            "Too low! Try a bigger number.\n",
            "Enter your guess (1-100): 15\n",
            "Too low! Try a bigger number.\n",
            "Enter your guess (1-100): 16\n",
            "Too low! Try a bigger number.\n",
            "Enter your guess (1-100): 17\n",
            "Too low! Try a bigger number.\n",
            "Enter your guess (1-100): 18\n",
            "Too low! Try a bigger number.\n",
            "Enter your guess (1-100): 19\n",
            "Congratulations! You won!\n",
            "Number of attempts: 12\n",
            "Game Over!\n"
          ]
        }
      ],
      "source": [
        "\n",
        "import random\n",
        "\n",
        "print(\"================================\")\n",
        "print(\"     NUMBER GUESSING GAME\")\n",
        "print(\"================================\")\n",
        "\n",
        "secret_number = random.randint(1, 100)\n",
        "attempts = 0\n",
        "\n",
        "while True:\n",
        "\n",
        "    guess = int(input(\"Enter your guess (1-100): \"))\n",
        "\n",
        "    attempts = attempts + 1\n",
        "\n",
        "    if guess == secret_number:\n",
        "        print(\"Congratulations! You won!\")\n",
        "        print(\"Number of attempts:\", attempts)\n",
        "        break\n",
        "\n",
        "    elif guess < secret_number:\n",
        "        print(\"Too low! Try a bigger number.\")\n",
        "\n",
        "    else:\n",
        "        print(\"Too high! Try a smaller number.\")\n",
        "\n",
        "print(\"Game Over!\")"
      ]
    }
  ]
}