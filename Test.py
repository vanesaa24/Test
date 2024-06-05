import pandas as pd

class DataExtractor:
    def __init__(self, expiredInvoices, new_invoices):
        self.expiredInvoices = expiredInvoices
        self.new_invoices = new_invoices

    def load(self,invoiceData):
        with open(invoiceData, 'rb') as loaded_new:
            self.new_invoices = load(loaded_new)

    def transform(self):
        df = []
        for i in self.new_invoices:
            invoice_id = int(i.id)
            created_on = pd.to_datetime(i.created_on)
            total = sum(j.unit_price * j.quantity for j in self.new_invoices)

            for j in i.items:
                item_id = j.id
                item_name = j.name
                item_type = {0: 'Material', 1: 'Equipment', 2: 'Service', 3: 'Other'}.get(j.type)
                unit_price = j.unit_price
                total_price = j.unit_price * j.quantity
                percentage_in_invoice = total_price / total
                is_expired = invoice_id in self.expiredInvoices

                df.append({
                    'invoice_id': invoice_id,
                    'created_on': created_on,
                    'invoiceitem_id': item_id,
                    'invoiceitem_name': item_name,
                    'type': item_type,
                    'unit_price': unit_price,
                    'total_price': total_price,
                    'percentage_in_invoice': percentage_in_invoice,
                    'is_expired': is_expired
                })
        df = pd.DataFrame(df)
        df = df.sort_values(by = ['invoice_id', 'invoiceitem_id'])
        return df


