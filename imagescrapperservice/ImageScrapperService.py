
from imagescrapper.ImageScrapper import ImageScrapper
from imagescrapperutils.ImageScrapperUtils import ImageScrapperUtils
class ImageScrapperService:
    
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper
    keyWord = ""
    fileLoc = ""
    image_name = ""
    header = ""
    '''def __main__(keyWord, image_name, fileLoc, header):
    keyWord = keyWord
    fileLoc = fileLoc
    image_name = keyWord
    dao = DAO
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper'''
    # you can change the query for the image  here
    
    #pdb.set_trace()
    
    def downloadImages( keyWord, header):
        print('keyWord',keyWord,'header',header)
        imgScrapper = ImageScrapper
        url = imgScrapper.createURL(keyWord)

        rawHtml = imgScrapper.get_RawHtml(url, header)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        print('rawHtml type',type(rawHtml))
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header)
        print('url', url,'\nimageURLList',imageURLList,'\nmasterListOfImages',masterListOfImages)
        return masterListOfImages

    def get_image_urls(keyWord, header):
        imgScrapper = ImageScrapper
        url = imgScrapper.createURL(keyWord)
        rawHtml = imgScrapper.get_RawHtml(url, header)

        imageURLList = imgScrapper.getimageUrlList(rawHtml)

        return imageURLList