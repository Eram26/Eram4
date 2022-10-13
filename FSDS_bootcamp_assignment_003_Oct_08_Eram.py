#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENTS - Compulsory
# ## Send it before 0000 hrs IST or 12 AM Wednesday
# 
# ## NOTE: Evaluation will be done before next class.
# 
# ## HOW TO SUBMIT: -
# Download this notebook, Solve it and upload in the google form given in the mail.

# ## Python String Manipulation
# 
# 1. Count the number of times `iNeuron` appears in the string.
# ```python
# text = "Welcome to iNeuron, You are a part of FSDS Bootcamp 2 in iNeuron. I hope you are enjoying the course by iNeuron"
# ```
# 2. Check if position `5` to `11` ends with the phrase `iNeuron.` in the string 
# ```python
# txt = "Hello, welcome to FSDS 2.0 at iNeuron."
# ```
# 3. Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if your name is Sunny Bhaveen Chandra, then the output should be S.B.Chandra.
# 
# 4. Join all items in a list into a string, using a hash(`#`) character as separator:
# ```python
# LIST = ["My", "name", "is", "Rishav", "Dash"]
# ```
# 5. Write example for the following string manipulation function,
# 
#   ```
#   - isdecimal()
#   - islower()
#   - isupper()
#   - isalpha()
#   - isnumeric()
# 
#   ```
# 6. Indian PAN card format follows the following formats - 
#     - `AYEPC7894X`
#     - `ABCDE9999Y`
#   Take user input for PAN_CARD and validate as per the above example.
# 

# In[1]:




text = "Welcome to iNeuron, You are a part of FSDS Bootcamp 2 in iNeuron. I hope you are enjoying the course by iNeuron"
text.count("iNeuron")


# In[2]:


#SOL 3
name =  input("enter your date of bith in format of : firstname/middle name/last name")
#indexing =0123456789
First_name=name[0:1]
middle_name=name[5:6]
last_name=name[9: ]
print(f"your first name is:  {First_name} middle name is :{middle_name} lastname is :{last_name} ")


# In[6]:


number="89"
number.isdecimal()


# In[9]:


name="india"
name.islower()


# In[14]:


name="INDIA"
name.isupper()


# In[17]:


name="india"
name.isalpha()


# In[19]:


data="889975"
data.isnumeric()


# In[24]:


#SOL 4
LIST = ["My", "name", "is", "Rishav", "Dash"]
"#".join(LIST)


# In[26]:


#SOL 2
txt = "Hello, welcome to FSDS 2.0 at iNeuron."
position=txt.endswith("iNeuron.")
print(position)


# In[27]:


#Sol 6
Pan_number= input("enter pan number in format: __________")
len(Pan_number)==10
if Pan_number[:5].isalpha():
  if Pan_number[5:8].isdigit(): 
    if Pan_number[9].isalpha():
  
        print(f"you have enter a correct pan no:{Pan_number}")
else:
  print("invalid input")


# In[ ]:




