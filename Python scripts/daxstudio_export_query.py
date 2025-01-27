import os
import subprocess
from datetime import datetime
from urllib.parse import quote


def authentication_mode(type, **kwargs):

    user_email = kwargs.get('user_email')
    password = kwargs.get('password')
    
    tenant_id = kwargs.get('tenant_id')
    client_id = kwargs.get('client_id')
    client_secret = kwargs.get('client_secret')

    if type == 'user_email':
        auth_str = f'-u "{user_email}" -p "{password}"'
        return auth_str

    if type == 'service_principal':
        auth_str = f'-u "app:{client_id}@{tenant_id}" -p "{client_secret}"'
        return auth_str
    
    else:
        raise ValueError(f'"{type}" is not a valid input. Select between "user_email" or "service_principal".')


def export_query_to_csv(auth_str, workspace_name, dataset_name, query, file_name):
    
    ts = datetime.now().strftime('%Y%m%d%H%M%S')
    output = os.path.join(OUTPUT_DIR, f'{file_name}_{ts}.csv')
    
    parsed_workspace_name = quote(workspace_name)
    conn_str = f'powerbi://api.powerbi.com/v1.0/myorg/{parsed_workspace_name}'

    cmd = f'{DSCMD_DIR} csv "{output}" -s "{conn_str}" -d "{dataset_name}" {auth_str} -q "{query}"'

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Command failed - {result.stdout}")
    else:
        print("Command executed successfully.")


if __name__ == '__main__':
    '''
    1) Export function example using user email and password:
    
    user_email = 'user_email@microsoft.com'
    password = 'password123'

    auth_str = authentication_mode('user_email', user_email=user_email, password=password)
    export_query_to_csv(auth_str, workspace_name, dataset_name, query)


    2) Export function example using tenant id, client id and client secret (service principal):
    
    tenant_id = 'azure-app-tenant-id'
    client_id = 'azure-app-client-id'
    client_secret = 'azure-app-secret-id'

    auth_str = authentication_mode('service_principal', tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
    export_query_to_csv(auth_str, workspace_name, dataset_name, query)

    Additional info:
    - Download of Dax Studio portable version: https://daxstudio.org/downloads/

    '''
    # Folder path to DAX Studio CMD .exe
    DSCMD_DIR = 'C:/Users/lamoras/Downloads/DaxStudioPortable/dscmd'

    # Folder path to export files
    OUTPUT_DIR = 'C:/Users/lamoras/Downloads'

    # Premium workspace and dataset info
    workspace_name = 'Power BI Workspace'
    dataset_name = 'Power BI Dataset'
    file_name = 'info_tables'
    query = 'EVALUATE INFO.TABLES()'
    
    user_email = 'user_name@microsoft.com'
    password = 'password123'

    auth_str = authentication_mode('user_email', user_email=user_email, password=password)

    export_query_to_csv(auth_str, workspace_name, dataset_name, query, file_name)
