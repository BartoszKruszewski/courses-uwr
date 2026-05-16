import { Dialog } from '@base-ui/react'

export interface SettingsConfirmationDialogProps {
  confirmLabel?: string
  description: string
  onConfirm: () => void
  onOpenChange: (open: boolean) => void
  open: boolean
  title: string
}

export function SettingsConfirmationDialog({
  confirmLabel = 'Confirm',
  description,
  onConfirm,
  onOpenChange,
  open,
  title,
}: SettingsConfirmationDialogProps) {
  return (
    <Dialog.Root open={open} onOpenChange={onOpenChange} modal>
      <Dialog.Portal keepMounted>
        <Dialog.Backdrop className="settings-dialog-backdrop" />
        <Dialog.Viewport className="settings-dialog-viewport">
          <Dialog.Popup className="settings-dialog-popup">
            <Dialog.Title className="settings-dialog-title">{title}</Dialog.Title>
            <Dialog.Description className="settings-dialog-description">
              {description}
            </Dialog.Description>

            <div className="settings-dialog-actions">
              <Dialog.Close className="settings-dialog-button settings-dialog-button-secondary">
                Cancel
              </Dialog.Close>
              <button
                type="button"
                className="settings-dialog-button settings-dialog-button-danger"
                onClick={onConfirm}
              >
                {confirmLabel}
              </button>
            </div>
          </Dialog.Popup>
        </Dialog.Viewport>
      </Dialog.Portal>
    </Dialog.Root>
  )
}