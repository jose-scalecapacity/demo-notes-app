from sst import App, Stack, Table, TableFieldType

app = App(name="my-sst-python-app")

class MyStack(Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.table = Table(self, "my-sst-table",
            fields={
                "id": TableFieldType.STRING
            },
            primary_index={"partition_key": "id"}
        )

app.stack(MyStack) 