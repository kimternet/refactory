import random

def convert_to_str_with_sign(temp):
   if temp.is_integer():
       if temp > 0:
           return f"+{int(temp)}"
       else:
           return f"{int(temp)}"
   else:
       if temp > 0:
           return f"+{temp:.1f}"
       else:
           return f"{temp:.1f}"

def convert_to_str_with_sign_answer(temp):
   if temp.is_integer():
       if temp >= 0:
           return f"{int(temp)}"
       else:
           return f"{int(temp)}"
   else:
       if temp >= 0:
           return f"{temp:.1f}"
       else:
           return f"{temp:.1f}"

def generate_table_stem(cities, max_temperatures, min_temperatures):
   table_stem = "<table style='border: 1px solid black; border-collapse: collapse; text-align: center; margin: 0 auto;'>"
   table_stem += "<tr style='background-color: lightgray;'>"
   table_stem += "<th style='padding: 5px;'>도시</th>"
   for city in cities:
       table_stem += f"<td style='padding: 5px;'>{city}</td>"
   table_stem += "</tr>"

   table_stem += "<tr>"
   table_stem += "<th style='padding: 5px;'>최고 기온 \\((°C)\\)</th>"
   for max_temp in max_temperatures:
       table_stem += f"<td style='padding: 5px;'>\\({convert_to_str_with_sign(max_temp)}\\)</td>"
   table_stem += "</tr>"

   table_stem += "<tr>"
   table_stem += "<th style='padding: 5px;'>최저 기온 \\((°C)\\)</th>"
   for min_temp in min_temperatures:
       table_stem += f"<td style='padding: 5px;'>\\({convert_to_str_with_sign(min_temp)}\\)</td>"
   table_stem += "</tr>"
   table_stem += "</table>"

   return table_stem