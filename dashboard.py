import papermill as pm

pm.execute_notebook(
   'dashboard.ipynb',
   'dashboard_output.ipynb',

   parameters=dict(bestand="dashboard_input.csv")
)