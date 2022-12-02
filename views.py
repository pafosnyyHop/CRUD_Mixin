from search import searc_object




class CreatMixin:
    def entry(self, brand: str, marka: str, year_of_issue: int, engine_volume: float, color: str, mileage: int, price: float) -> dict:
        """Создает dict и добавляет его в атрибут объекта Cars"""
        object_ = dict(id = self.get_id(), brand = brand, marka = marka, year_of_issue = year_of_issue, engine_volume = engine_volume, color = color, mileage = mileage, price = price)
        body_type = input('Выберите тип кузова (station wagon sedan, coupe, hatchback, minivan, SUV, pickup): ').strip().lower()
        if body_type == 'station wagon sedan' or body_type == 'coupe' or body_type == 'hatcback' or body_type == 'minivan'  or body_type == 'suv' or body_type == 'pickup':
            object_['body_type'] = body_type
        else:
            raise ValueError('Такого типа кузова в списке нет!')
        engine_volume = round(float(engine_volume), 1)
        price = round(float(price), 2)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}


    @staticmethod
    def get_data():
        '''возвращает список со словарями из json'''
        import json
        with open('/home/hello/Рабочий стол/hakatoon_CRUDmixin/data.json') as file:
            return json.load(file)


class RetrieveMixin:
    def list(self) -> dict:
        '''проходит циклом по атрбуту объекта Cars'''
        res = []
        for obj in self.objects:
            res.append({'id': obj['id'],'brand': obj['brand'], 'marka': obj['marka'], 'price': obj['price']})
        return {'status': 200, 'msg': res}
    @searc_object
    def detail(self, id: int, **kwargs):
        
        obj = kwargs['object_']
        if obj:
            return {'status': 200, 'msg': obj}
        return {'status': 404, 'msg': 'NOT FOUND!!!'}

class UpdateMixin:
    @searc_object
    def patch(self, id: int, **kwargs) -> dict:
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return {'status': 206, 'msg': obj}
        return {'status': 404, 'msg': 'NOT FOUND!!!!'}

class DestroyMixin:
    @searc_object
    def delete(self, id: int, **kwargs) -> dict:
        obj = kwargs.get('object_')
        if obj:
            self.objects.remove(obj)
            return {'status': 204, 'msg': 'Deleted'}
        return {'staus': 404, 'msg': 'NOT FOUND!!!!!!'}

class Cars(CreatMixin, RetrieveMixin, UpdateMixin, DestroyMixin):
    def __init__(self):
        self.objects = self.get_data()


    @staticmethod
    def get_id() -> int:
        
        with open('id.txt', 'r') as file:
            id = int(file.read())  
            id += 1
        with open('id.txt', 'w') as file:
            file.write(str(id))
        return id
        
    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved!'
    


