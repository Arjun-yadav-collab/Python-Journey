{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b2021e2e-c485-4d5c-ac63-f8cf5887e23b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "current year :  4\n",
      "enter category :  obc\n",
      "last year percentage 45\n",
      "last year passing status :  pass\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are not eligible\n"
     ]
    }
   ],
   "source": [
    "current_year= input(\"current year : \").lower()\n",
    "cate = input(\"enter category : \").lower()\n",
    "pre_per = float(input(\"last year percentage\"))\n",
    "pre_year = str(input(\"last year passing status : \")).lower()\n",
    "sch = {\n",
    "    \"sc\": 20000,\n",
    "    \"st\": 30000,\n",
    "    \"obc\": 10000,    \n",
    "}\n",
    "if cate in sch:\n",
    "    num = sch[cate]\n",
    "    if pre_per > 50 and pre_per < 60:\n",
    "        print(\"you get an scholarship\", num)\n",
    "    elif pre_per >= 60 and pre_per < 75:\n",
    "        num += (num* 10) / 100\n",
    "        print(\"you get an scholarship\", num)\n",
    "    elif pre_per >= 75 and pre_per < 85:\n",
    "        num += (num * 20) / 100\n",
    "        print(\"you get an scholarship\", num)\n",
    "    elif pre_per >= 85 and pre_per < 95:\n",
    "        num += (num * 50) / 100\n",
    "        print(\"you get an scholarship\", num)\n",
    "    elif pre_per >= 95:\n",
    "        num *= 2\n",
    "        print(\"you get an scholarship\", num)\n",
    "    else:\n",
    "        print(\"you are not eligible\")\n",
    "else:\n",
    "    print(\"you are not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90798cdf-6bf5-4b21-8f42-dc4c0b2d3a96",
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
