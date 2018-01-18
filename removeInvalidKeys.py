from sets import Set
import os

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

def getValidLines(f, validKeys):
	validLines = []
	for line in f:
		if isValidLine(line, validKeys):
			validLines.append(line)
	return validLines

def isValidLine(line, validKeys):
	if(len(line)) < 3:
		return

	fileKey = line.split()[0]
	for key in validKeys:
		if line.endswith(".") and line.startswith(key):
			return True
		elif (fileKey == key):
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
	targetDir = "/Users/nmazaheri/Documents/git/lib-loc-account-recovery/src/main/resources/com/blizzard/account/messages"
	validLoc = Set(['cant.login.merge.title.choose','cant.login.desc.new','account.creation.continueToManagement', 'account.creation.ingame.error.header', 'account.creation.oauth.divider.text', 'authenticator.button.resync.authenticator', 'authenticator.remove.success.desc', 'authenticator.remove.success.title', 'authenticator.str.resync.intro', 'authenticator.str.resync.reasoning', 'authenticator.str.resync.success.intro', 'authenticator.str.resync.success.title', 'authenticator.str.resync.title', 'cancel', 'cant.login.authenticator.form.bnet', 'cant.login.title', 'close', 'common.blizzard', 'common.grammar.colon', 'common.required', 'common.securitInput', 'common.securityInput.placeholder', 'continue', 'email.change.info.format', 'email.change.info.invalid', 'email.change.info.mismatch', 'error.email.invalid', 'error.field.requiredFields', 'error.payment.tw.taxInvoice', 'error.personal.verification.invalid.referer', 'error.personal.verification.invalid.result', 'error.required', 'error.sms.integration.not.have.authenticator', 'error.term', 'login', 'loginSupport.changePassword.page', 'loginSupport.changePassword.subtitle', 'loginSupport.changeSuccess.passwordChanged', 'loginSupport.mobile.country', 'loginSupport.segregated.reactivate.intro', 'loginSupport.verification.license.field', 'loginSupport.verification.license.note', 'loginSupport.verification.nid.field', 'loginSupport.verification.nid.option', 'loginSupport.verification.personalVerification.option', 'loginSupport.verification.photoid.field', 'loginSupport.verification.photoid.option', 'loginSupport.verification.select.choose', 'loginSupport.verification.select.where', 'loginSupport.verification.sqa.field', 'loginSupport.verification.sqa.option', 'loginSupport.verification.sqa.question', 'page.management.addNeteaseToken.serialInput.label', 'page.security.add.ba.authCodeLabel', 'page.security.add.ba.authCodeLabel2', 'page.security.option.mobile.alert.change.send.desc', 'page.security.option.mobile.alert.change.send.enter', 'page.security.option.mobile.alert.register.again', 'password.change.alt.confirmNewPassword', 'password.change.alt.newPassword', 'password.change.alt.oldPassword', 'password.change.confirmNewPassword', 'password.change.info.invalid', 'password.change.info.mismatch', 'password.change.newPassword', 'password.change.note', 'password.change.oldPassword', 'password.change.strength', 'password.change.subtitle', 'passwordrequirements.alphanumeric', 'passwordrequirements.length', 'passwordrequirements.similarname', 'passwordrequirements.specialchars', 'retreive.email.desc.success1', 'retreive.email.desc.success2', 'retreive.email.sub.success', 'retrieve.account.no.account', 'retrieve.account.recover', 'retrieve.account.success', 'retrieve.account.success.management', 'retrieve.confirm.desc', 'retrieve.login.input', 'retrieve.success.title', 'retrieve.title', 'search.account', 'streamlined.creation.alt.jCaptcha', 'streamlined.creation.jCaptcha', 'streamlined.creation.password.fair', 'streamlined.creation.password.short', 'streamlined.creation.password.strength', 'streamlined.creation.password.strong', 'streamlined.creation.password.weak', 'submit', 'support.account.recovery.contact.html', 'support.account.recovery.kr.alternative.button', 'support.account.recovery.kr.alternative.desc', 'support.account.recovery.success.desc', 'support.account.recovery.success.title', 'support.account.support.ticket.submitted.contact.html', 'support.account.support.ticket.submitted.desc', 'support.account.support.ticket.submitted.title', 'support.account.unlock.success.desc', 'support.account.unlock.success.title', 'support.arw.form.captcha.desc', 'support.arw.form.captcha.placeholder', 'support.arw.form.phone', 'support.arw.got.hacked.desc.html', 'support.arw.lost.account.name.page.desc', 'support.arw.lost.account.name.page.sms.required', 'support.arw.lost.account.name.page.title', 'support.arw.page.desc', 'support.arw.page.title', 'support.captcha.read', 'support.captcha.try', 'support.help.contact.support', 'support.help.different.email', 'support.help.different.issue', 'support.personal.verification.alt.link.game.key', 'support.personal.verification.alt.link.game.key.tooltip', 'support.personal.verification.alt.link.ipin', 'support.personal.verification.alt.link.ipin.tooltip', 'support.personal.verification.alt.link.nid', 'support.personal.verification.alt.link.nid.tooltip', 'support.personal.verification.alt.link.no.game.key', 'support.personal.verification.alt.link.no.ipin', 'support.personal.verification.alt.link.sqa', 'support.personal.verification.game.key.label.html', 'support.personal.verification.game.key.note', 'support.personal.verification.game.key.placeholder', 'support.personal.verification.kr.next.page', 'support.personal.verification.nid.label', 'support.personal.verification.nid.placeholder', 'support.personal.verification.sqa.placeholder', 'support.personal.verification.title.account.recovery', 'support.personal.verification.title.change.password', 'support.personal.verification.title.unlock.account', 'support.remove.auth.desc', 'support.remove.auth.form.doc.type', 'support.remove.auth.form.file.selected', 'support.remove.auth.form.id', 'support.remove.auth.form.phone', 'support.remove.auth.form.phone.placeholder', 'support.remove.auth.form.removal.label', 'support.remove.auth.form.removal.reason', 'support.remove.auth.form.upload.image', 'support.remove.auth.form.upload.image.type', 'support.remove.auth.title', 'support.retrieve.email.contact.html', 'support.retrieve.email.success.desc', 'support.retrieve.email.success.reset.btn', 'support.retrieve.email.success.titile', 'support.security.verify.authenticator.alt.link', 'support.security.verify.authenticator.desc', 'support.security.verify.authenticator.tooltip', 'support.security.verify.sms.alt.link', 'support.security.verify.sms.number.desc', 'support.security.verify.sms.tooltip', 'support.untrusted-device.desc', 'support.untrusted-device.title', 'support.verify.code.action.password.change', 'support.verify.code.action.remove.auth', 'support.verify.code.action.unlock', 'support.verify.code.code.sent.email', 'support.verify.code.headline.email', 'support.verify.code.headline.mobile', 'support.verify.code.method.email', 'support.verify.code.method.mobile', 'support.verify.code.nid.label', 'support.verify.code.nid.placeholder', 'support.verify.code.placeholder', 'support.verify.code.resend.email.html', 'support.verify.code.resend.mobile.html', 'support.verify.code.sent', 'support.verify.code.subcategory.remove.auth', 'support.verify.code.throttled', 'title.home', 'url.bnet.account.', 'url.bnet.home.', 'url.support.', 'url.support.article.acceptable.id.', 'url.support.cant.login.help.article.', 'validation.personal.description', 'validation.proceed'])

	if not os.path.isdir(targetDir):
		print "ERROR: invalid path = " + targetDir
		exit(1)

	print ("deleting unused keys from loc based on:")
	print ",".join(validLoc)

	print
	for subdir, dirs, files in os.walk(targetDir):
		for file in files:
			fileLocation = os.path.join(subdir, file)
			clean(fileLocation, validLoc)

	print
	for d in getEmptyDirectories(targetDir):
		print "removing directory = " + d
		os.rmdir(d)