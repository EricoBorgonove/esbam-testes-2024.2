import requests

#URL da base da API ReqRes

BASE_URL = "https://reqres.in/api/users"
# python -m venv ambiente
# . ambiente/bin/activate

def create_user():
    new_user ={
    "name": "Gabriel",
    "job": "student"
    }
    # response = requests.post(BASE_URL,json = new_user)
    response = requests.post(BASE_URL, json=new_user, 
                             headers={'Content-Type': 'application/json'}, 
                             timeout=10)

    if response.status_code == 201:
        user = response.json()
        print("Usuário Criado com sucesso:", user)
        return user['id']
    else:
        print("Erro ao criar usuário", response.status_code, response.text)
        return None
    
def get_user (user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
        
    if response.status_code == 200:
        user = response.json()
        print("dados do Usuário:", user)
        return user
    else:
        print ("usuário não encontrado", response.status_code, 
                                    response.text)
        return None
        
def update_user (user_id):
    updated_data={
        "name": "Gabriel Araujo Silva",
        "job": "data anaticts expecialist"
    }
    response = requests.put(f"{BASE_URL}/{user_id}", json= updated_data,
                            headers={'Content-Type': 'application/json'}, 
                            timeout=10) 
    if response.status_code == 200:
        user = response.json()
        print("Usuário Atualizado com sucesso:", user)
        return user
    else:
        print ("Erro ao atualizar o usuário", response.status_code, 
                                    response.text)
        return None  
    
def delete_user (user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
        
    if response.status_code == 204:
        
        print("Usuário deletado com sucesso")
        return True
    else:
        print ("Erro ao deletar Usuário", response.status_code, 
                                    response.text)
        return False  
    
# def test_user2():
#     user = get_user(2)
    
#     assert user['id'] == 2
#     assert user["first_name"] == "Janet"
#     assert user["email"] == "janet.weaver@reqres.in"
     
        
if __name__ == "__main__":
    print(f"CREATE \n")
    user_id = create_user()
    print(f"READ \n")
    get_user(user_id)
    print(f"UPDATE\n")
    update_user(user_id)
    print(f"DELETE \n")
    delete_user(user_id)
    # print("TEST \n")
    # test_user2()