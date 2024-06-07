# streamlit_local_db
Basic streamlit app to connect with local ms sql server db.

Starting by following doc on https://docs.streamlit.io/develop/tutorials/databases/mssql

Make sure that the user has db permission to select, insert or what you need to do via the app 😁. Can be set via Microsoft SQL Server Management Studio. 



# .streamlit/secrets.toml
Make a secrets file ".streamlit/secrets.toml" under the apps root dir so you can connect to your local db.  

<span style="color: red;font-weight:bold;">
--> Add this secrets file to .gitignore !!! <--
</span> (don't commit secrets to your repo 💀)

```yaml
# .streamlit/secrets.toml
server = "server_name"
database = "db_name"
username = "user_name"
password = "xxx"
```

# conda env / dependencies
Run "conda env create -f conda_env.yaml" from conda_env folder in anaconda prompt to create env, or just check the used env dependenices in the .yaml. 
```terminal
conda env create -f conda_env.yaml
```

# run app
Run the app from terminal with 
````
streamlit run app.py
````