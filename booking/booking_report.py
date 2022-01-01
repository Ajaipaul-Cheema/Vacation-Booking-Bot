from selenium.webdriver.remote.webdriver import WebElement
import pandas as pd


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name(
            'sr_property_block'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element_by_class_name(
                'sr-hotel__name'
            ).get_attribute('innerHTML').strip()
            final_hotel_name = hotel_name.replace("&amp;", "&")
            hotel_price = deal_box.find_element_by_class_name(
                'bui-price-display__value'
            ).get_attribute('innerHTML').strip()
            final_hotel_price = hotel_price.replace("&nbsp;", "$")

            hotel_score = deal_box.get_attribute(
                'data-score'
            ).strip()

            collection.append(
                [hotel_name, final_hotel_price, hotel_score]
            )
        df = pd.DataFrame(collection, columns=['Hotel Name', 'Hotel Price', 'Hotel Score'])
        df.to_excel('YourBookings.xlsx', index=False, header=True)
        return collection
