from turtle import title
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from common.database.firebase import articles

from modules.moduleSearchArticle.searchArticle import SearchArticle

from common.widgets.cardShoppingWidget.cardShoppingWidget import CardShoppingWidget
from common.entities.shopping_car_entity import ShoppingCardEntity

from common.values import strings
from .adapter.shoppingAux import ShoppingAux
from .widgets.mount import MountPay


class ShoppingCarMDCard(MDCard,ShoppingAux):

    listShoppingCar:list = []
    dialog:MDDialog = None
    def __init__(self,**kargs) -> None:
        super(ShoppingCarMDCard,self).__init__(**kargs)
        
        self.setupKeyBoard()
        Clock.schedule_once(lambda *args:self.setFocusCodeBar(*args))

    def setupKeyBoard(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        if keycode[1] == 'w':
            self.player1.center_y += 10
        elif keycode[1] == 's':
            self.player1.center_y -= 10
        elif keycode[1] == 'up':
            self.player2.center_y += 10
        elif keycode[1] == 'down':
            self.player2.center_y -= 10
        return True
    
    
    def addArticleShoppingCar(self,cardArticle:CardShoppingWidget):
        self.ids.shopping_car_container.add_widget(cardArticle)
        self.listShoppingCar.append(cardArticle)
        self.setTotalShoppingCar()
    
    def clearFields(self):
        self.ids.text_field_code_bar.text = ""

    def setFocusCodeBar(self,*args):
        self.ids.text_field_code_bar.focus = True
    
    def openMountPay(self):
        self.closeDialog()
        if self.listShoppingCar.__len__() == 0:
            self.dialog = MDDialog(
                    title = strings.msg_shopping_car_is_empty,
                    buttons = [
                        MDFlatButton(text = strings.btn_yes, on_press = self.closeDialog)
                    ])
            self.dialog.open()
        else:
            content = MountPay(self)
            self.dialog = MDDialog(
                    title = strings.title_mount_pay,
                    type = "custom",
                    content_cls = content,
                    buttons = [
                        MDFlatButton(text = strings.btn_no, on_press = self.closeDialog),
                        MDFlatButton(text = strings.btn_yes,on_press = self.printerTicketSale)
                    ])
            self.dialog.open()


    def openSearchArticle(self):
        searchArticleMenu = SearchArticle()
        self.dialog = MDDialog(
            title = strings.title_search_article,
            type = "custom",
            content_cls = searchArticleMenu,
            buttons = [
                MDFlatButton(
                    text = strings.btn_exit,
                    on_press =self.closeDialog
                )
            ]
        )
        self.dialog.open()

    def searchArticle(self,codeBar:str):
        if codeBar.__len__() > 0:
            if articles.existsArticle(codeBar):
                article = articles.getArticleById(codeBar)
                shoppingEntity = ShoppingCardEntity(
                    idArticle = article.id,
                    photoUrlArticle = article.photoUrl,
                    nameArticle = article.name,
                    amountArticle = 1.0,
                    priceUniArticle = article.price)
                cardShopping = CardShoppingWidget(shoppingEntity,self)
                self.addArticleShoppingCar(cardShopping)
            else:
                self.openDialog(strings.msg_article_not_found)
            self.clearFields()
        else:
            self.openDialog(strings.msg_code_bar_search_is_empty)
        Clock.schedule_once(lambda *args:self.setFocusCodeBar(*args))

    def openDialog(self,title):
        self.closeDialog()
        self.dialog = MDDialog(title = title,buttons = [
            MDFlatButton(
                text = strings.btn_yes,
                on_press = self.closeDialog
                )
        ])
        self.dialog.open()
    
    def closeDialog(self,*args):
        if self.dialog is not None:
            self.dialog.dismiss(force = True)

    def clearShoppingCar(self):
        for widget in self.listShoppingCar:
            self.ids.shopping_car_container.remove_widget(widget)
        self.listShoppingCar.clear()
        self.setTotalShoppingCar()
    
    def printerTicketSale(self,*args):
        self.closeDialog()

    ##################
    ## ShoppingAux
    ##################

    def removeItemShoppingCar(self,cardWidget:CardShoppingWidget):
        self.listShoppingCar.remove(cardWidget)
        self.ids.shopping_car_container.remove_widget(cardWidget)
        self.setTotalShoppingCar()

    def setTotalShoppingCar(self):
        total = 0.0
        for cardArticle in self.listShoppingCar:
            total += cardArticle.getTotal()
        self.ids.label_total_pay.text = total.__str__()

    def finishShoppingCar(self,pay:float):
        for widget in self.listShoppingCar:
            if articles.deleteAmountArticle(
                codeBar = widget.shopping.idArticle,
                amount = widget.shopping.amountArticle
            ) == False:
                print("el articulo no fue localizado")
        self.closeDialog()
        self.dialog = MDDialog(
            title = strings.msg_ask_print_ticket_sale,
            buttons = [
                MDFlatButton(
                    text = strings.btn_no, on_press = self.closeDialog),
                MDFlatButton(
                    text = strings.btn_yes,on_press = self.printerTicketSale
                )
            ]   
        )
        self.dialog.open()
        self.clearShoppingCar()
        Snackbar(text=strings.msg_success_sale_shopping_car).open()
        
    def getTotal(self)->float:
        total = 0.0
        for cardArticle in self.listShoppingCar:
            total += cardArticle.getTotal()
        return total