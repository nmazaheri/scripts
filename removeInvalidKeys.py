from sets import Set
import os
import sys

validLoc = Set(['maintenance.message','maintenance.title','error.throttled.limit','error.throttled.desc','error.403.desc','error.wow-conversion.account.notfound','error.sms.integration.field.required.numeric','error.password.invalid.similar','error.password.invalid.length','invalidPuncs','error.password.invalid.chars.required','error.password.mustMatch','error.field.notnumeric','error.file.size','error.file.type','error.form.authValue.invalid','error.support.resync.other','error.support.resync.tokenNotAttached','error.support.resync.serialNumberNotFound','cant.login.merge.title.not.join','cant.login.hacked.title','support.ineligible.title','contactSupport.page','back.to.blizzard','error.addGame.gameKey.length','contactSupport.page','support.throttled.desc','error.throttle.limit','password.change.short','password.change.strong','password.change.fair','password.change.weak','loginSupport.changePassword.page','cant.login.option.forgot.account.name.html','cant.login.option.remove.authenticator.html','cant.login.option.account.locked.html','cant.login.option.forgot.password.html','cant.login.desc.select.an.option','cant.login.merge.title.choose','cant.login.desc.new','account.creation.continueToManagement', 'account.creation.ingame.error.header', 'account.creation.oauth.divider.text', 'authenticator.button.resync.authenticator', 'authenticator.remove.success.desc', 'authenticator.remove.success.title', 'authenticator.str.resync.intro', 'authenticator.str.resync.reasoning', 'authenticator.str.resync.success.intro', 'authenticator.str.resync.success.title', 'authenticator.str.resync.title', 'cancel', 'cant.login.authenticator.form.bnet', 'cant.login.title', 'close', 'common.blizzard', 'common.grammar.colon', 'common.required', 'common.securitInput', 'common.securityInput.placeholder', 'continue', 'email.change.info.format', 'email.change.info.invalid', 'email.change.info.mismatch', 'error.email.invalid', 'error.field.requiredFields', 'error.payment.tw.taxInvoice', 'error.personal.verification.invalid.referer', 'error.personal.verification.invalid.result', 'error.required', 'error.sms.integration.not.have.authenticator', 'error.term', 'login', 'loginSupport.changePassword.page', 'loginSupport.changePassword.subtitle', 'loginSupport.changeSuccess.passwordChanged', 'loginSupport.mobile.country', 'loginSupport.segregated.reactivate.intro', 'loginSupport.verification.license.field', 'loginSupport.verification.license.note', 'loginSupport.verification.nid.field', 'loginSupport.verification.nid.option', 'loginSupport.verification.personalVerification.option', 'loginSupport.verification.photoid.field', 'loginSupport.verification.photoid.option', 'loginSupport.verification.select.choose', 'loginSupport.verification.select.where', 'loginSupport.verification.sqa.field', 'loginSupport.verification.sqa.option', 'loginSupport.verification.sqa.question', 'page.management.addNeteaseToken.serialInput.label', 'page.security.add.ba.authCodeLabel', 'page.security.add.ba.authCodeLabel2', 'page.security.option.mobile.alert.change.send.desc', 'page.security.option.mobile.alert.change.send.enter', 'page.security.option.mobile.alert.register.again', 'password.change.alt.confirmNewPassword', 'password.change.alt.newPassword', 'password.change.alt.oldPassword', 'password.change.confirmNewPassword', 'password.change.info.invalid', 'password.change.info.mismatch', 'password.change.newPassword', 'password.change.note', 'password.change.oldPassword', 'password.change.strength', 'password.change.subtitle', 'passwordrequirements.alphanumeric', 'passwordrequirements.length', 'passwordrequirements.similarname', 'passwordrequirements.specialchars', 'retreive.email.desc.success1', 'retreive.email.desc.success2', 'retreive.email.sub.success', 'retrieve.account.no.account', 'retrieve.account.recover', 'retrieve.account.success', 'retrieve.account.success.management', 'retrieve.confirm.desc', 'retrieve.login.input', 'retrieve.success.title', 'retrieve.title', 'search.account', 'streamlined.creation.alt.jCaptcha', 'streamlined.creation.jCaptcha', 'streamlined.creation.password.fair', 'streamlined.creation.password.short', 'streamlined.creation.password.strength', 'streamlined.creation.password.strong', 'streamlined.creation.password.weak', 'submit', 'support.account.recovery.contact.html', 'support.account.recovery.kr.alternative.button', 'support.account.recovery.kr.alternative.desc', 'support.account.recovery.success.desc', 'support.account.recovery.success.title', 'support.account.support.ticket.submitted.contact.html', 'support.account.support.ticket.submitted.desc', 'support.account.support.ticket.submitted.title', 'support.account.unlock.success.desc', 'support.account.unlock.success.title', 'support.arw.form.captcha.desc', 'support.arw.form.captcha.placeholder', 'support.arw.form.phone', 'support.arw.got.hacked.desc.html', 'support.arw.lost.account.name.page.desc', 'support.arw.lost.account.name.page.sms.required', 'support.arw.lost.account.name.page.title', 'support.arw.page.desc', 'support.arw.page.title', 'support.captcha.read', 'support.captcha.try', 'support.help.contact.support', 'support.help.different.email', 'support.help.different.issue', 'support.personal.verification.alt.link.game.key', 'support.personal.verification.alt.link.game.key.tooltip', 'support.personal.verification.alt.link.ipin', 'support.personal.verification.alt.link.ipin.tooltip', 'support.personal.verification.alt.link.nid', 'support.personal.verification.alt.link.nid.tooltip', 'support.personal.verification.alt.link.no.game.key', 'support.personal.verification.alt.link.no.ipin', 'support.personal.verification.alt.link.sqa', 'support.personal.verification.game.key.label.html', 'support.personal.verification.game.key.note', 'support.personal.verification.game.key.placeholder', 'support.personal.verification.kr.next.page', 'support.personal.verification.nid.label', 'support.personal.verification.nid.placeholder', 'support.personal.verification.sqa.placeholder', 'support.personal.verification.title.account.recovery', 'support.personal.verification.title.change.password', 'support.personal.verification.title.unlock.account', 'support.remove.auth.desc', 'support.remove.auth.form.doc.type', 'support.remove.auth.form.file.selected', 'support.remove.auth.form.id', 'support.remove.auth.form.phone', 'support.remove.auth.form.phone.placeholder', 'support.remove.auth.form.removal.label', 'support.remove.auth.form.removal.reason', 'support.remove.auth.form.upload.image', 'support.remove.auth.form.upload.image.type', 'support.remove.auth.title', 'support.retrieve.email.contact.html', 'support.retrieve.email.success.desc', 'support.retrieve.email.success.reset.btn', 'support.retrieve.email.success.titile', 'support.security.verify.authenticator.alt.link', 'support.security.verify.authenticator.desc', 'support.security.verify.authenticator.tooltip', 'support.security.verify.sms.alt.link', 'support.security.verify.sms.number.desc', 'support.security.verify.sms.tooltip', 'support.untrusted-device.desc', 'support.untrusted-device.title', 'support.verify.code.action.password.change', 'support.verify.code.action.remove.auth', 'support.verify.code.action.unlock', 'support.verify.code.code.sent.email', 'support.verify.code.headline.email', 'support.verify.code.headline.mobile', 'support.verify.code.method.email', 'support.verify.code.method.mobile', 'support.verify.code.nid.label', 'support.verify.code.nid.placeholder', 'support.verify.code.placeholder', 'support.verify.code.resend.email.html', 'support.verify.code.resend.mobile.html', 'support.verify.code.sent', 'support.verify.code.subcategory.remove.auth', 'support.verify.code.throttled', 'title.home', 'validation.personal.description', 'validation.proceed','url.bnet.account.', "url.support."])

def clean(fileLocation, validKeys):
	# capture all valid keys into memory then rewrite the file
	f=open(fileLocation, 'r+')
	validLines = getValidLines(f, validKeys)

	if validLines:
		print "processing " + fileLocation
		f.truncate()
	else:
		print "removing " + fileLocation
		os.remove(fileLocation)
		return

	f.close()
	f=open(fileLocation, 'w')
	for line in validLines:
		f.write(line)
	f.close()

def getValidLines(file, validKeys):
	validLines = []
	for line in file:
		if isValidLine(line, validKeys):
			validLines.append(line)
	return validLines

def isValidLine(line, validKeys):
	if(len(line)) < 3:
		return

	currentKey = line.split()[0]
	for validKey in validKeys:
		if validKey.endswith(".") and line.startswith(validKey):
			return True
		elif (currentKey == validKey):
			return True

	return False

def getEmptyDirectories(dir):
	result = []
	for root, dirs, files in os.walk(targetDir,topdown=False):
		for name in dirs:
			fname = os.path.join(root,name)
			if not os.listdir(fname): #to check wither the dir is empty
				result.append(fname)
	return Set(result)

if __name__ == '__main__':
	# inputs
	if len(sys.argv) != 2:
		print "ERROR: invalid arguments: " + str(sys.argv)

	targetDir = sys.argv[1]

	if not os.path.isdir(targetDir):
		print "ERROR: invalid path = " + targetDir
		exit(1)

	print ("valid keys which will not be deleted:")
	print ",".join(validLoc)

	print
	for subdir, dirs, files in os.walk(targetDir):
		for file in files:
			fileLocation = os.path.join(subdir, file)
			clean(fileLocation, validLoc)

	print
	print "removing empty directories:"
	for d in getEmptyDirectories(targetDir):
		print d
		os.rmdir(d)