{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "63b3f3c4-3b2e-404e-8de1-89aa216d6943",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter the first value= 25\n",
      "enter the second value= 15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HCF= 5\n"
     ]
    }
   ],
   "source": [
    "var_1=int(input(\"enter the first value=\"))\n",
    "var_2=int(input(\"enter the second value=\"))\n",
    "\n",
    "while var_2 !=0:\n",
    "    var_1,var_2=var_2,var_1%var_2\n",
    "print(\"HCF=\",var_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4de5d15b-3371-47b6-a0f3-f5358536707e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
