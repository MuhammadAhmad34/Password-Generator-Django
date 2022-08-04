from django.shortcuts import render
import random


def home(request):
    data = {}
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars = ['''!''', '''@''', '''#''', '''$''', '''%''', '''^''',
             '''&''', '''*''', '''(''', ''')''', '''_''', '''+''']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    password = []
    if request.method == "POST":

        try:
            Limit = int(request.POST.get('passLimit'))
            typePass = request.POST.get('PassType')
            if typePass == 'weak':
                print("Weak")

                if Limit < 8:
                    data.update(
                        {"result": "Password Minimum Limit 8 chracters"})
                else:

                    for i in range(0, Limit):
                        # print(random.choice(alphabets))
                        password.append(random.choice(alphabets))
                data.update({"Password": password})
                return render(request, 'index.html', data)
                
            elif typePass == 'Normal':

                print("Normal")
                if Limit < 8:
                    data.update(
                        {"result": "Password Minimum Limit 8 chracters"})
                else:
                    alphabets.extend(numbers)
                    for i in range(0, Limit):
                        # print(random.choice(alphabets))
                        password.append(random.choice(alphabets))
                        data.update({"Password": password})
                    return render(request, 'index.html', data)

            else:
                print("Strong")
                
                if Limit < 8:
                    data.update(
                        {"result": "Password Minimum Limit 8 chracters"})
                else:
                    chars.extend(numbers)
                    alphabets.extend(chars)
                    for i in range(0, Limit):
                        # print(random.choice(alphabets))
                        password.append(random.choice(alphabets))
                    data.update({"Password": password})
                return render(request, 'index.html', data)

        except Exception as e:
            data.update({"error": "Pleas enter valid Input"})
            return render(request, 'index.html', data)
            
    return render(request, 'index.html', data)
