 #este es un comentario
 response = client.chat.completions.create(
 model="gpt-4o-mini-2024-07-18",
 response_format={ "type": "json_object" },
 messages=[
 {
 "role": "system",
 "content": context },
 {
 "role": "user",
 "content" : usertask },
 {
 "role": "user",
 "content": userquery }
 ],
 temperature=1,
 max_tokens=16384,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0
 )
#*--- post process response message to eliminate garbage from the JSON file
 jsonStr=response.choices[0].message.content